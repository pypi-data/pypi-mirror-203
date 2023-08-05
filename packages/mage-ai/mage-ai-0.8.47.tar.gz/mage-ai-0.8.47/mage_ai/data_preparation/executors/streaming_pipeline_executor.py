from contextlib import redirect_stderr, redirect_stdout
from mage_ai.data_preparation.executors.pipeline_executor import PipelineExecutor
from mage_ai.data_preparation.logging.logger import DictLogger
from mage_ai.data_preparation.models.constants import BlockType
from mage_ai.data_preparation.models.pipeline import Pipeline
from mage_ai.data_preparation.shared.stream import StreamToLogger
from mage_ai.shared.hash import merge_dict
from typing import Callable, Dict, List, Union
import asyncio
import logging
import os
import yaml


class StreamingPipelineExecutor(PipelineExecutor):
    def __init__(self, pipeline: Pipeline, **kwargs):
        super().__init__(pipeline, **kwargs)
        # TODO: Support custom log destination for streaming pipelines
        self.parse_and_validate_blocks()

    def parse_and_validate_blocks(self):
        """
        Find the first valid streaming pipeline is in the structure:
        source -> transformer -> sink
        """
        blocks = self.pipeline.blocks_by_uuid.values()
        source_blocks = []
        sink_blocks = []
        transformer_blocks = []
        for b in blocks:
            if b.type == BlockType.DATA_LOADER:
                if len(b.upstream_blocks or []) > 0:
                    raise Exception(f'Data loader {b.uuid} can\'t have upstream blocks.')
                if len(b.downstream_blocks or []) != 1:
                    raise Exception(f'Data loader {b.uuid} must have one transformer or data'
                                    ' exporter as the downstream block.')
                source_blocks.append(b)
            if b.type == BlockType.DATA_EXPORTER:
                if len(b.downstream_blocks or []) > 0:
                    raise Exception(f'Data expoter {b.uuid} can\'t have downstream blocks.')
                if len(b.upstream_blocks or []) != 1:
                    raise Exception(f'Data loader {b.uuid} must have a transformer or data'
                                    ' exporter as the upstream block.')
                sink_blocks.append(b)
            if b.type == BlockType.TRANSFORMER:
                if len(b.downstream_blocks or []) != 1:
                    raise Exception(
                        f'Transformer {b.uuid} should (only) have one downstream block.',
                    )
                if len(b.upstream_blocks or []) != 1:
                    raise Exception(f'Transformer {b.uuid} should (only) have one upstream block.')
                transformer_blocks.append(b)

        if len(source_blocks) != 1:
            raise Exception('Please provide (only) one data loader block as the source.')

        if len(transformer_blocks) > 1:
            raise Exception('Please provide no more than one transformer block.')

        if len(sink_blocks) != 1:
            raise Exception('Please provide (only) one data expoter block as the sink.')

        self.source_block = source_blocks[0]
        self.sink_block = sink_blocks[0]
        self.transformer_block = transformer_blocks[0] if len(transformer_blocks) > 0 else None

    def execute(
        self,
        build_block_output_stdout: Callable[..., object] = None,
        global_vars: Dict = None,
        **kwargs,
    ) -> None:
        # TODOs:
        # 1. Support multiple sources and sinks
        # 2. Support flink pipeline

        tags = self._build_tags(**kwargs)
        if build_block_output_stdout:
            stdout_logger = logging.getLogger('streaming_pipeline_executor')
            self.logger = DictLogger(stdout_logger)
            stdout = build_block_output_stdout(self.pipeline.uuid)
        else:
            self.logger = DictLogger(self.logger_manager.logger, logging_tags=tags)
            stdout = StreamToLogger(self.logger, logging_tags=tags)
        try:
            with redirect_stdout(stdout):
                with redirect_stderr(stdout):
                    self.__execute_in_python(
                        build_block_output_stdout=build_block_output_stdout,
                    )
        except Exception as e:
            if not build_block_output_stdout:
                self.logger.exception(
                        f'Failed to execute streaming pipeline {self.pipeline.uuid}',
                        **merge_dict(dict(error=e), tags),
                    )
            raise e

    def __execute_in_python(self, build_block_output_stdout: Callable[..., object] = None):
        from mage_ai.streaming.sources.base import SourceConsumeMethod
        from mage_ai.streaming.sources.source_factory import SourceFactory
        from mage_ai.streaming.sinks.sink_factory import SinkFactory
        source_config = yaml.safe_load(self.source_block.content)
        sink_config = yaml.safe_load(self.sink_block.content)
        source = SourceFactory.get_source(
            source_config,
            checkpoint_path=os.path.join(
                self.pipeline.pipeline_variables_dir,
                'streaming_checkpoint',
            ),
        )
        sink = SinkFactory.get_sink(
            sink_config,
            buffer_path=os.path.join(
                self.pipeline.pipeline_variables_dir,
                'buffer',
            ),
        )

        def handle_batch_events(messages: List[Union[Dict, str]], **kwargs):
            if self.transformer_block is not None:
                execute_block_kwargs = dict(
                    global_vars=kwargs,
                    input_args=[messages],
                    logger=self.logger,
                )
                if build_block_output_stdout:
                    execute_block_kwargs['build_block_output_stdout'] = build_block_output_stdout
                messages = self.transformer_block.execute_block(
                    **execute_block_kwargs,
                )['output']
            sink.batch_write(messages)

        async def handle_event_async(message, **kwargs):
            if self.transformer_block is not None:
                execute_block_kwargs = dict(
                    global_vars=kwargs,
                    input_args=[[message]],
                    logger=self.logger,
                )
                if build_block_output_stdout:
                    execute_block_kwargs['build_block_output_stdout'] = build_block_output_stdout
                messages = self.transformer_block.execute_block(
                    **execute_block_kwargs,
                )['output']
            sink.batch_write(messages)

        # Long running method
        if source.consume_method == SourceConsumeMethod.BATCH_READ:
            source.batch_read(handler=handle_batch_events)
        elif source.consume_method == SourceConsumeMethod.READ_ASYNC:
            asyncio.run(source.read_async(handler=handle_event_async))

    def __excute_in_flink(self):
        """
        TODO: Implement this method
        """
        pass
