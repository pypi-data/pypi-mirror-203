(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[5912],{44162:function(n,t,e){"use strict";e.d(t,{HC:function(){return A},Kf:function(){return s},Nk:function(){return p},PY:function(){return f},gE:function(){return m},jv:function(){return b},nz:function(){return v},oh:function(){return a},qn:function(){return l},t1:function(){return h},y9:function(){return T}});var r=e(9518),o=e(23831),i=e(86422),c=e(73942),u=e(49125),d=e(90880),a=68;function l(n,t){var e,r,c=((null===t||void 0===t||null===(e=t.theme)||void 0===e?void 0:e.borders)||o.Z.borders).light,u=((null===t||void 0===t||null===(r=t.theme)||void 0===r?void 0:r.monotone)||o.Z.monotone).grey500,d=t||{},a=d.blockColor,l=d.isSelected,s=d.theme;return l?c=((null===s||void 0===s?void 0:s.content)||o.Z.content).active:i.tf.TRANSFORMER===n||a===i.Lq.PURPLE?(c=((null===s||void 0===s?void 0:s.accent)||o.Z.accent).purple,u=((null===s||void 0===s?void 0:s.accent)||o.Z.accent).purpleLight):i.tf.DATA_EXPORTER===n||a===i.Lq.YELLOW?(c=((null===s||void 0===s?void 0:s.accent)||o.Z.accent).yellow,u=((null===s||void 0===s?void 0:s.accent)||o.Z.accent).yellowLight):i.tf.DATA_LOADER===n||a===i.Lq.BLUE?(c=((null===s||void 0===s?void 0:s.accent)||o.Z.accent).blue,u=((null===s||void 0===s?void 0:s.accent)||o.Z.accent).blueLight):i.tf.SENSOR===n||a===i.Lq.PINK?(c=((null===s||void 0===s?void 0:s.accent)||o.Z.accent).pink,u=((null===s||void 0===s?void 0:s.accent)||o.Z.accent).pinkLight):i.tf.DBT===n?(c=((null===s||void 0===s?void 0:s.accent)||o.Z.accent).dbt,u=((null===s||void 0===s?void 0:s.accent)||o.Z.accent).dbtLight):i.tf.EXTENSION===n||a===i.Lq.TEAL?(c=((null===s||void 0===s?void 0:s.accent)||o.Z.accent).teal,u=((null===s||void 0===s?void 0:s.accent)||o.Z.accent).tealLight):(i.tf.SCRATCHPAD===n||a===i.Lq.GREY||i.tf.CUSTOM===n&&!a)&&(c=((null===s||void 0===s?void 0:s.content)||o.Z.content).default,u=((null===s||void 0===s?void 0:s.accent)||o.Z.accent).contentDefaultTransparent),{accent:c,accentLight:u}}var s=(0,r.css)([""," "," "," "," "," "," ",""],(0,d.eR)(),(function(n){return!n.selected&&!n.hasError&&"\n    border-color: ".concat(l(n.blockType,n).accentLight,";\n  ")}),(function(n){return n.selected&&!n.hasError&&"\n    border-color: ".concat(l(n.blockType,n).accent,";\n  ")}),(function(n){return!n.selected&&n.hasError&&"\n    border-color: ".concat((n.theme.accent||o.Z.accent).negativeTransparent,";\n  ")}),(function(n){return n.selected&&n.hasError&&"\n    border-color: ".concat((n.theme.borders||o.Z.borders).danger,";\n  ")}),(function(n){return n.dynamicBlock&&"\n    border-style: dashed !important;\n  "}),(function(n){return n.dynamicChildBlock&&"\n    border-style: dotted !important;\n  "})),p=r.default.div.withConfig({displayName:"indexstyle__ContainerStyle",componentId:"sc-s5rj34-0"})(["border-radius:","px;position:relative;"],c.n_),f=r.default.div.withConfig({displayName:"indexstyle__HiddenBlockContainerStyle",componentId:"sc-s5rj34-1"})([""," border-radius:","px;border-style:",";border-width:","px;",""],s,c.n_,c.M8,c.mP,(function(n){return"\n    background-color: ".concat((n.theme||o.Z).background.content,";\n\n    &:hover {\n      border-color: ").concat(l(n.blockType,n).accent,";\n    }\n  ")})),v=r.default.div.withConfig({displayName:"indexstyle__BlockHeaderStyle",componentId:"sc-s5rj34-2"})([""," border-top-left-radius:","px;border-top-right-radius:","px;border-top-style:",";border-top-width:","px;border-left-style:",";border-left-width:","px;border-right-style:",";border-right-width:","px;padding:","px;position:sticky;top:-5px;"," ",""],s,c.n_,c.n_,c.M8,c.mP,c.M8,c.mP,c.M8,c.mP,u.iI,(function(n){return"\n    background-color: ".concat((n.theme||o.Z).background.content,";\n  ")}),(function(n){return n.zIndex&&"\n    z-index: ".concat(6+(n.zIndex||0),";\n  ")})),b=r.default.div.withConfig({displayName:"indexstyle__CodeContainerStyle",componentId:"sc-s5rj34-3"})([""," border-left-style:",";border-left-width:","px;border-right-style:",";border-right-width:","px;padding-bottom:","px;padding-top:","px;position:relative;"," "," .line-numbers{opacity:0;}&.selected{.line-numbers{opacity:1 !important;}}"],s,c.M8,c.mP,c.M8,c.mP,u.iI,u.iI,(function(n){return"\n    background-color: ".concat((n.theme.background||o.Z.background).codeTextarea,";\n  ")}),(function(n){return!n.hasOutput&&"\n    border-bottom-left-radius: ".concat(c.n_,"px;\n    border-bottom-right-radius: ").concat(c.n_,"px;\n    border-bottom-style: ").concat(c.M8,";\n    border-bottom-width: ").concat(c.mP,"px;\n  ")})),m=r.default.div.withConfig({displayName:"indexstyle__BlockDivider",componentId:"sc-s5rj34-4"})(["align-items:center;display:flex;height:","px;justify-content:center;position:relative;z-index:8;bottom:","px;&:hover{"," .block-divider-inner{","}}"],2*u.iI,.5*u.iI,(function(n){return n.additionalZIndex>0&&"\n      z-index: ".concat(8+n.additionalZIndex,";\n    ")}),(function(n){return"\n        background-color: ".concat((n.theme.text||o.Z.text).fileBrowser,";\n      ")})),h=r.default.div.withConfig({displayName:"indexstyle__BlockDividerInner",componentId:"sc-s5rj34-5"})(["height 1px;width:100%;position:absolute;z-index:-1;top:","px;"],1.5*u.iI),T=r.default.div.withConfig({displayName:"indexstyle__CodeHelperStyle",componentId:"sc-s5rj34-6"})(["margin-bottom:","px;padding-bottom:","px;",""],u.cd*u.iI,u.iI,(function(n){return"\n    border-bottom: 1px solid ".concat((n.theme.borders||o.Z.borders).medium,";\n    padding-left: ").concat(n.normalPadding?u.iI:a,"px;\n  ")})),A=r.default.div.withConfig({displayName:"indexstyle__TimeTrackerStyle",componentId:"sc-s5rj34-7"})(["bottom:","px;left:","px;position:absolute;"],1*u.iI,a)},43032:function(n,t,e){"use strict";e.d(t,{Cl:function(){return u},Nk:function(){return d},ZG:function(){return c}});var r=e(9518),o=e(23831),i=e(49125),c=1.5*i.iI,u=1*c+i.iI/2,d=r.default.div.withConfig({displayName:"indexstyle__ContainerStyle",componentId:"sc-uvd91-0"})([".row:hover{","}"],(function(n){return"\n      background-color: ".concat((n.theme.interactive||o.Z.interactive).hoverBackground,";\n    ")}))},86422:function(n,t,e){"use strict";e.d(t,{$W:function(){return p},DA:function(){return s},HX:function(){return b},J8:function(){return v},Lq:function(){return a},Qj:function(){return m},Ut:function(){return E},V4:function(){return A},VZ:function(){return f},dO:function(){return l},f2:function(){return T},iZ:function(){return h},t6:function(){return c},tf:function(){return d}});var r,o,i,c,u=e(82394);!function(n){n.PYTHON="python",n.R="r",n.SQL="sql",n.YAML="yaml"}(c||(c={}));var d,a,l=(r={},(0,u.Z)(r,c.PYTHON,"PY"),(0,u.Z)(r,c.R,"R"),(0,u.Z)(r,c.SQL,"SQL"),(0,u.Z)(r,c.YAML,"YAML"),r);!function(n){n.CHART="chart",n.CUSTOM="custom",n.DATA_EXPORTER="data_exporter",n.DATA_LOADER="data_loader",n.DBT="dbt",n.EXTENSION="extension",n.SCRATCHPAD="scratchpad",n.SENSOR="sensor",n.TRANSFORMER="transformer"}(d||(d={})),function(n){n.BLUE="blue",n.GREY="grey",n.PINK="pink",n.PURPLE="purple",n.TEAL="teal",n.YELLOW="yellow"}(a||(a={}));var s,p=[d.CHART,d.CUSTOM,d.DATA_EXPORTER,d.DATA_LOADER,d.SCRATCHPAD,d.SENSOR,d.TRANSFORMER],f=[d.DATA_EXPORTER,d.DATA_LOADER],v=[d.DATA_EXPORTER,d.DATA_LOADER,d.TRANSFORMER],b=[d.DATA_EXPORTER,d.DATA_LOADER,d.DBT,d.TRANSFORMER],m=[d.CHART,d.SCRATCHPAD,d.SENSOR],h=[d.EXTENSION,d.SCRATCHPAD];!function(n){n.EXECUTED="executed",n.FAILED="failed",n.NOT_EXECUTED="not_executed",n.UPDATED="updated"}(s||(s={}));var T=[d.CUSTOM,d.DATA_EXPORTER,d.TRANSFORMER],A=(o={},(0,u.Z)(o,d.CUSTOM,"Custom"),(0,u.Z)(o,d.DATA_EXPORTER,"Data exporter"),(0,u.Z)(o,d.DATA_LOADER,"Data loader"),(0,u.Z)(o,d.EXTENSION,"Extension"),(0,u.Z)(o,d.SCRATCHPAD,"Scratchpad"),(0,u.Z)(o,d.SENSOR,"Sensor"),(0,u.Z)(o,d.TRANSFORMER,"Transformer"),o),E=[d.DATA_LOADER,d.TRANSFORMER,d.DATA_EXPORTER,d.SENSOR];i={},(0,u.Z)(i,d.DATA_EXPORTER,"DE"),(0,u.Z)(i,d.DATA_LOADER,"DL"),(0,u.Z)(i,d.SCRATCHPAD,"SP"),(0,u.Z)(i,d.SENSOR,"SR"),(0,u.Z)(i,d.TRANSFORMER,"TF")},50094:function(n,t,e){"use strict";e.r(t);var r=e(77837),o=e(75582),i=e(82394),c=e(38860),u=e.n(c),d=e(82684),a=e(92083),l=e.n(a),s=e(9518),p=e(21679),f=e(16634),v=e(67971),b=e(87372),m=e(87465),h=e(41788),T=e(55378),A=e(86673),E=e(82531),R=e(23831),O=e(67400),_=e(43032),x=e(92953),g=e(44162),y=e(24224),Z=e(28598);function S(n,t){var e=Object.keys(n);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(n);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(n,t).enumerable}))),e.push.apply(e,r)}return e}function D(n){for(var t=1;t<arguments.length;t++){var e=null!=arguments[t]?arguments[t]:{};t%2?S(Object(e),!0).forEach((function(t){(0,i.Z)(n,t,e[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(n,Object.getOwnPropertyDescriptors(e)):S(Object(e)).forEach((function(t){Object.defineProperty(n,t,Object.getOwnPropertyDescriptor(e,t))}))}return n}function C(n){var t=n.pipeline,e=(0,d.useContext)(s.ThemeContext),r=(0,d.useState)(null),c=r[0],u=r[1],a=t.uuid,h=E.ZP.pipelines.detail(a,{includes_content:!1,includes_outputs:!1},{revalidateOnFocus:!1}).data,S=(0,d.useMemo)((function(){return D(D({},null===h||void 0===h?void 0:h.pipeline),{},{uuid:a})}),[h,a]),C=E.ZP.pipeline_schedules.pipelines.list(a).data,P=(0,d.useMemo)((function(){return null===C||void 0===C?void 0:C.pipeline_schedules}),[C]),N=(0,d.useMemo)((function(){return(0,y.HK)(null===S||void 0===S?void 0:S.blocks,(function(n){return n.uuid}))||{}}),[S]),L={pipeline_uuid:a};(c||0===c)&&(L.pipeline_schedule_id=Number(c));var k=E.ZP.monitor_stats.detail("block_run_count",L),j=k.data,w=k.mutate,I=((null===j||void 0===j?void 0:j.monitor_stat)||{}).stats,M=(0,d.useMemo)((function(){for(var n=new Date,t=[],e=0;e<90;e++)t.unshift(n.toISOString().split("T")[0]),n.setDate(n.getDate()-1);return t}),[]),X=(0,d.useMemo)((function(){if(I)return Object.entries(I).reduce((function(n,t){var e=(0,o.Z)(t,2),r=e[0],c=e[1].data,u=M.map((function(n){return D({date:n},c[n]||{})}));return D(D({},n),{},(0,i.Z)({},r,u))}),{})}),[M,I]),H=(0,d.useMemo)((function(){var n=[];return n.push({bold:!0,label:function(){return"Monitors"}}),n}),[]);return(0,Z.jsx)(m.Z,{breadcrumbs:H,monitorType:x.a.BLOCK_RUNS,pipeline:S,subheader:(0,Z.jsx)(v.Z,{children:(0,Z.jsxs)(T.Z,{backgroundColor:R.Z.interactive.defaultBackground,label:"Trigger:",onChange:function(n){var t=n.target.value;"initial"!==t?(u(t),w(t)):(w(),u(null))},value:c||"initial",children:[(0,Z.jsx)("option",{value:"initial",children:"All"}),P&&P.map((function(n){return(0,Z.jsx)("option",{value:n.id,children:n.name},n.id)}))]})}),children:(0,Z.jsx)(A.Z,{mx:2,children:X&&Object.entries(X).map((function(n){var t,r,i=(0,o.Z)(n,2),c=i[0],u=i[1];return(0,Z.jsxs)(A.Z,{mt:3,children:[(0,Z.jsxs)(v.Z,{alignItems:"center",children:[(0,Z.jsx)(A.Z,{mx:1,children:(0,Z.jsx)(f.Z,{color:(0,g.qn)(null===(t=N[c])||void 0===t?void 0:t.type,{blockColor:null===(r=N[c])||void 0===r?void 0:r.color,theme:e}).accent,size:_.ZG,square:!0})}),(0,Z.jsx)(b.Z,{level:4,children:c})]}),(0,Z.jsx)(A.Z,{mt:1,children:(0,Z.jsx)(p.Z,{colors:O.BAR_STACK_COLORS,data:u,getXValue:function(n){return n.date},height:200,keys:O.BAR_STACK_STATUSES,margin:{bottom:30,left:35,right:0,top:10},tooltipLeftOffset:x.C,xLabelFormat:function(n){return l()(n).format("MMM DD")}})})]},c)}))})})}C.getInitialProps=function(){var n=(0,r.Z)(u().mark((function n(t){var e;return u().wrap((function(n){for(;;)switch(n.prev=n.next){case 0:return e=t.query.pipeline,n.abrupt("return",{pipeline:{uuid:e}});case 2:case"end":return n.stop()}}),n)})));return function(t){return n.apply(this,arguments)}}(),t.default=(0,h.Z)(C)},83542:function(n,t,e){(window.__NEXT_P=window.__NEXT_P||[]).push(["/pipelines/[pipeline]/monitors/block-runs",function(){return e(50094)}])}},function(n){n.O(0,[3850,2083,5896,2714,2344,4506,6166,6214,2249,7400,9774,2888,179],(function(){return t=83542,n(n.s=t);var t}));var t=n.O();_N_E=t}]);