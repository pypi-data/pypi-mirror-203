(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[3853],{1210:function(e,n,t){"use strict";t.d(n,{Z:function(){return Z}});var r=t(82394),i=t(21831),o=t(82684),c=t(47999),l=t(28358),u=t(93461),d=t(57384),s=t(12344),a=t(72454),f=t(28598);function p(e,n){var t=e.children;return(0,f.jsx)(a.HS,{ref:n,children:t})}var h=o.forwardRef(p),b=t(32063),v=t(15270),m=t(82531),g=t(66166),x=t(3055),j=t(49125),k=t(91427),y=t(24141);function O(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function w(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?O(Object(t),!0).forEach((function(n){(0,r.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):O(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var Z=function(e){var n,t=e.after,r=e.afterHidden,p=e.afterWidth,O=e.afterWidthOverride,Z=e.before,_=e.beforeWidth,P=e.breadcrumbs,C=e.children,I=e.errors,S=e.headerMenuItems,D=e.navigationItems,E=e.setErrors,W=e.subheaderChildren,H=e.title,M=e.uuid,N=(0,y.i)().width,A="dashboard_after_width_".concat(M),q="dashboard_before_width_".concat(M),Y=(0,o.useRef)(null),T=(0,o.useState)(O?p:(0,k.U2)(A,p)),B=T[0],R=T[1],F=(0,o.useState)(!1),U=F[0],z=F[1],G=(0,o.useState)(Z?Math.max((0,k.U2)(q,_),13*j.iI):null),X=G[0],J=G[1],L=(0,o.useState)(!1),Q=L[0],V=L[1],K=(0,o.useState)(null)[1],$=m.ZP.projects.list({},{revalidateOnFocus:!1}).data,ee=null===$||void 0===$?void 0:$.projects,ne=[];P?ne.push.apply(ne,(0,i.Z)(P)):(null===ee||void 0===ee?void 0:ee.length)>=1&&ne.push.apply(ne,[{label:function(){var e;return null===(e=ee[0])||void 0===e?void 0:e.name},linkProps:{href:"/"}},{bold:!0,label:function(){return H}}]),(0,o.useEffect)((function(){null===Y||void 0===Y||!Y.current||U||Q||null===K||void 0===K||K(Y.current.getBoundingClientRect().width)}),[U,B,Q,X,Y,K,N]),(0,o.useEffect)((function(){U||(0,k.t8)(A,B)}),[r,U,B,A]),(0,o.useEffect)((function(){Q||(0,k.t8)(q,X)}),[Q,X,q]);var te=(0,g.Z)(p);return(0,o.useEffect)((function(){O&&te!==p&&R(p)}),[O,p,te]),(0,f.jsxs)(f.Fragment,{children:[(0,f.jsx)(d.Z,{title:H}),(0,f.jsx)(s.Z,{breadcrumbs:ne,menuItems:S,project:null===ee||void 0===ee?void 0:ee[0],version:null===ee||void 0===ee||null===(n=ee[0])||void 0===n?void 0:n.version}),(0,f.jsxs)(a.Nk,{children:[0!==(null===D||void 0===D?void 0:D.length)&&(0,f.jsx)(a.lm,{children:(0,f.jsx)(v.Z,{navigationItems:D})}),(0,f.jsx)(u.Z,{flex:1,flexDirection:"column",children:(0,f.jsxs)(b.Z,{after:t,afterHeightOffset:x.Mz,afterHidden:r,afterMousedownActive:U,afterWidth:B,before:Z,beforeHeightOffset:x.Mz,beforeMousedownActive:Q,beforeWidth:a.k1+(Z?X:0),hideAfterCompletely:!0,leftOffset:Z?a.k1:null,mainContainerRef:Y,setAfterMousedownActive:z,setAfterWidth:R,setBeforeMousedownActive:V,setBeforeWidth:J,children:[W&&(0,f.jsx)(h,{children:W}),C]})})]}),I&&(0,f.jsx)(c.Z,{disableClickOutside:!0,isOpen:!0,onClickOutside:function(){return null===E||void 0===E?void 0:E(null)},children:(0,f.jsx)(l.Z,w(w({},I),{},{onClose:function(){return null===E||void 0===E?void 0:E(null)}}))})]})}},2850:function(e,n,t){"use strict";t.d(n,{M:function(){return l},W:function(){return c}});var r=t(9518),i=t(23831),o=t(3055),c=34*t(49125).iI,l=r.default.div.withConfig({displayName:"indexstyle__BeforeStyle",componentId:"sc-12ee2ib-0"})(["min-height:calc(100vh - ","px);",""],o.Mz,(function(e){return"\n    border-left: 1px solid ".concat((e.theme.borders||i.Z.borders).medium,";\n  ")}))},79585:function(e,n,t){"use strict";t.d(n,{DQ:function(){return s},HY:function(){return c},SA:function(){return a},WH:function(){return o},eC:function(){return u},fF:function(){return l},tC:function(){return d}});var r=t(81132),i=t(9736),o="Workspace",c="Preferences",l="Git settings",u="Users",d="Account",s="Profile",a=function(e){var n=e.owner,t=e.roles,a=[{linkProps:{href:"/settings/workspace/preferences"},uuid:c}];n&&a.push({linkProps:{href:"/settings/workspace/users"},uuid:u}),(!(0,i.YB)()||t<=r.No.EDITOR)&&a.push({linkProps:{href:"/settings/workspace/sync-data"},uuid:l});var f=[{items:a,uuid:o}];return(0,i.YB)()?f.concat([{items:[{linkProps:{href:"/settings/account/profile"},uuid:s}],uuid:d}]):f}},30775:function(e,n,t){"use strict";t.d(n,{Z:function(){return w}});var r=t(1210),i=t(82394),o=t(12691),c=t.n(o),l=t(10919),u=t(86673),d=t(19711),s=t(9518),a=t(23831),f=t(49125),p=t(90880),h=(f.iI,s.default.div.withConfig({displayName:"indexstyle__SectionTitleStyle",componentId:"sc-1y8dyue-0"})(["padding:","px ","px;"],1*f.iI,2.5*f.iI)),b=s.default.div.withConfig({displayName:"indexstyle__ItemStyle",componentId:"sc-1y8dyue-1"})([""," padding:","px ","px;"," ",""],(0,p.eR)(),1.5*f.iI,2.5*f.iI,(function(e){return!e.selected&&"\n    &:hover {\n      background-color: ".concat((e.theme.background||a.Z.background).codeArea,";\n    }\n  ")}),(function(e){return e.selected&&"\n    background-color: ".concat((e.theme.background||a.Z.background).codeTextarea,";\n  ")})),v=t(28598),m=t(82684);function g(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function x(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?g(Object(t),!0).forEach((function(n){(0,i.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):g(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var j=function(e){var n=e.isItemSelected,t=e.sections;return(0,v.jsx)(u.Z,{py:f.Gg,children:null===t||void 0===t?void 0:t.map((function(e){var t=e.items,r=e.title,i=e.uuid;return(0,v.jsxs)(u.Z,{children:[(0,v.jsx)(h,{children:(0,v.jsx)(d.ZP,{bold:!0,muted:!0,small:!0,uppercase:!0,children:r?r():i})}),null===t||void 0===t?void 0:t.map((function(e){var t=e.label,r=e.linkProps,o=e.onClick,u=e.uuid,d=t?t():u,s=(0,v.jsx)(b,{selected:null===n||void 0===n?void 0:n(x(x({},e),{},{uuidWorkspace:i})),children:d});return r?(0,m.createElement)(c(),x(x({},r),{},{key:u,passHref:!0}),(0,v.jsx)(l.Z,{block:!0,noHoverUnderline:!0,noOutline:!0,sameColorAsText:!0,children:s})):(0,v.jsx)(l.Z,{block:!0,noHoverUnderline:!0,noOutline:!0,onClick:o,preventDefault:!0,sameColorAsText:!0,children:s},u)}))]},i)}))})},k=t(2850),y=t(79585),O=t(9736);var w=function(e){var n=e.after,t=e.afterHidden,i=e.children,o=e.uuidItemSelected,c=e.uuidWorkspaceSelected,l=(0,O.PR)()||{};return(0,v.jsx)(r.Z,{after:n,afterHidden:!n||t,afterWidth:n?50*f.iI:0,afterWidthOverride:!0,before:(0,v.jsx)(k.M,{children:(0,v.jsx)(j,{isItemSelected:function(e){var n=e.uuid,t=e.uuidWorkspace;return c===t&&o===n},sections:(0,y.SA)(l)})}),beforeWidth:k.W,title:"Settings",uuid:"settings/index",children:i})}},38341:function(e,n,t){"use strict";var r=t(21831),i=t(82394),o=t(26304),c=(t(82684),t(9518)),l=t(67971),u=t(86673),d=t(19711),s=t(23831),a=t(10503),f=t(73942),p=t(49125),h=t(28598),b=["beforeIcon","checked","disabled","errorMessage","label","labelDescription","large","meta","monospace","onClick","required","small","warning","xsmall"];function v(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function m(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?v(Object(t),!0).forEach((function(n){(0,i.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):v(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var g=c.default.div.withConfig({displayName:"Checkbox__CheckboxContainer",componentId:"sc-ujqx42-0"})(["display:inline-block;vertical-align:middle;cursor:pointer;"]),x=c.default.div.withConfig({displayName:"Checkbox__ErrorContainer",componentId:"sc-ujqx42-1"})(["margin-top:4px;"]),j=c.default.input.withConfig({displayName:"Checkbox__HiddenCheckbox",componentId:"sc-ujqx42-2"})(["border:0;clip:rect(0 0 0 0);clippath:inset(50%);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px;",""],(function(e){return e.notClickable&&"\n    background-color: ".concat((e.theme.content||s.Z.content).disabled,"\n    border-color: ").concat((e.theme.content||s.Z.content).disabled,"\n\n    &:hover {\n      cursor: not-allowed;\n    }\n  ")})),k=c.default.div.withConfig({displayName:"Checkbox__StyledCheckbox",componentId:"sc-ujqx42-3"})(["border-radius:","px;height:","px;transition:all 150ms;width:","px;svg{position:relative;visibility:",";}"," "," "," "," input[disabled]{cursor:default;}"," ",""],.5*p.iI,2*p.iI,2*p.iI,(function(e){return e.checked||e.required?"visible":"hidden"}),(function(e){return e.large&&"\n    svg {\n      left: -4px;\n      top: -8px;\n    }\n  "}),(function(e){return!e.checked&&"\n    background-color: ".concat((e.theme.background||s.Z.background).popup,";\n    border: ").concat(f.PV,"px ").concat(f.M8," ").concat((e.theme.content||s.Z.content).muted,";\n  ")}),(function(e){return e.checked&&"\n    background-color: ".concat((e.theme.interactive||s.Z.interactive).checked,";\n    border: ").concat(f.YF,"px ").concat(f.M8," transparent;\n  ")}),(function(e){return e.required&&"\n    background-color: ".concat((e.theme.content||s.Z.content).disabled,";\n    border: ").concat(f.YF,"px ").concat(f.M8," transparent;\n  ")}),(function(e){return e.disabled&&"\n    background-color: ".concat((e.theme.content||s.Z.content).disabled,";\n    border-color: ").concat((e.theme.content||s.Z.content).disabled,";\n\n    &:hover {\n      cursor: not-allowed;\n    }\n  ")}),(function(e){return e.warning&&"\n    background-color: ".concat((e.theme.accent||s.Z.accent).warning,";\n    border-color: ").concat((e.theme.interactive||s.Z.interactive).defaultBorder,"\n  ")})),y=c.default.label.withConfig({displayName:"Checkbox__LabelStyle",componentId:"sc-ujqx42-4"})(["-ms-flex-direction:column;align-items:center;display:flex;flex-direction:column;flex-direction:row;&:hover{cursor:pointer;}"]);n.Z=function(e){var n=e.beforeIcon,t=e.checked,i=e.disabled,c=e.errorMessage,s=e.label,f=e.labelDescription,v=e.large,O=e.meta,w=e.monospace,Z=void 0!==w&&w,_=e.onClick,P=e.required,C=e.small,I=void 0!==C&&C,S=e.warning,D=e.xsmall,E=void 0!==D&&D,W=(0,o.Z)(e,b),H=S||!!(c||O&&O.touched&&O.error);return(0,h.jsxs)(h.Fragment,{children:[(0,h.jsxs)(y,{onClick:function(e){e.preventDefault(),_&&!i&&_(e)},children:[(0,h.jsxs)(g,{children:[(0,h.jsx)(j,m(m({},W),{},{disabled:i?"disabled":void 0,notClickable:i})),(0,h.jsx)(k,{checked:t,disabled:i,large:v,required:P,warning:H,children:(0,h.jsx)(a.Jr,{size:p.iI*(v?3:2)})})]}),n&&(0,h.jsx)(u.Z,{ml:1,children:(0,h.jsx)(l.Z,{children:n})}),s&&(0,h.jsxs)(u.Z,{pl:1,children:["string"===typeof s&&(0,h.jsx)(d.ZP,{disabled:i,lineThrough:i,monospace:Z,small:I,xsmall:E,children:s}),"string"!==typeof s&&s,f&&(0,h.jsx)(d.ZP,{muted:!0,small:!0,children:f})]})]}),(c||O&&O.touched&&O.error)&&(0,h.jsx)(x,{children:(0,h.jsx)(d.ZP,{small:!0,warning:!0,children:c?(0,r.Z)(c):O.error})})]})}},42949:function(e,n,t){"use strict";t.r(n);var r=t(77837),i=t(38860),o=t.n(i),c=t(82684),l=t(38341),u=t(67971),d=t(41788),s=t(30775),a=t(86673),f=t(11366),p=t(49125),h=t(79585),b=t(91427),v=t(28598);function m(){var e=(0,c.useState)(!!(0,b.U2)(f.kY)),n=e[0],t=e[1];return(0,v.jsx)(s.Z,{uuidItemSelected:h.HY,uuidWorkspaceSelected:h.WH,children:(0,v.jsx)(a.Z,{p:p.cd,children:(0,v.jsx)(u.Z,{alignItems:"center",children:(0,v.jsx)(l.Z,{checked:n,label:"Automatically use randomly generated name for blocks created in the future",onClick:function(){t(!n),(0,b.t8)(f.kY,!n)}})})})})}m.getInitialProps=(0,r.Z)(o().mark((function e(){return o().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.abrupt("return",{});case 1:case"end":return e.stop()}}),e)}))),n.default=(0,d.Z)(m)},11366:function(e,n,t){"use strict";t.d(n,{H8:function(){return i},g6:function(){return o},kY:function(){return r}});var r="automatically_name_blocks",i="pipeline_edit_before_tab_selected",o="pipeline_edit_hidden_blocks"},33323:function(e,n,t){(window.__NEXT_P=window.__NEXT_P||[]).push(["/settings/workspace/preferences",function(){return t(42949)}])}},function(e){e.O(0,[3850,2344,4506,9774,2888,179],(function(){return n=33323,e(e.s=n);var n}));var n=e.O();_N_E=n}]);