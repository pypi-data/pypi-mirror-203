(self.webpackChunkcodechecker=self.webpackChunkcodechecker||[]).push([[680],{33657:(t,e,r)=>{var n=r(8081),i=r(23645)(n);i.push([t.id,"",""]),t.exports=i},41449:(t,e,r)=>{var n=r(8081),i=r(23645)(n);i.push([t.id,".link[data-v-6a6c9fd7]{text-decoration:none;color:inherit}.link[data-v-6a6c9fd7]:hover{color:var(--v-primary-lighten1)}.num-of-failed-files[data-v-6a6c9fd7]{cursor:pointer}.interval-selector[data-v-6a6c9fd7]{position:absolute;right:50px;top:0px;z-index:100}.interval-selector .interval[data-v-6a6c9fd7]{width:250px;border:1px dashed gray;padding:6px}.interval-selector .resolution[data-v-6a6c9fd7]{width:120px}",""]),t.exports=i},57769:(t,e,r)=>{var n=r(8081),i=r(23645)(n);i.push([t.id,".v-card__title[data-v-6ce34b56]{word-break:break-word}.day-col[data-v-6ce34b56]:hover{opacity:.8}",""]),t.exports=i},82460:(t,e,r)=>{var n=r(8081),i=r(23645)(n);i.push([t.id,".v-card[data-v-24a4abfb]{border:thin solid rgba(0,0,0,.12)}",""]),t.exports=i},46684:(t,e,r)=>{var n=r(33657);n.__esModule&&(n=n.default),"string"==typeof n&&(n=[[t.id,n,""]]),n.locals&&(t.exports=n.locals),(0,r(45346).Z)("e3618bca",n,!0,{})},42671:(t,e,r)=>{var n=r(41449);n.__esModule&&(n=n.default),"string"==typeof n&&(n=[[t.id,n,""]]),n.locals&&(t.exports=n.locals),(0,r(45346).Z)("b17e700e",n,!0,{})},89943:(t,e,r)=>{var n=r(57769);n.__esModule&&(n=n.default),"string"==typeof n&&(n=[[t.id,n,""]]),n.locals&&(t.exports=n.locals),(0,r(45346).Z)("295ca9e6",n,!0,{})},22351:(t,e,r)=>{var n=r(82460);n.__esModule&&(n=n.default),"string"==typeof n&&(n=[[t.id,n,""]]),n.locals&&(t.exports=n.locals),(0,r(45346).Z)("d150c126",n,!0,{})},84680:(t,e,r)=>{"use strict";r.r(e),r.d(e,{default:()=>Rt}),r(26699),r(91058),r(19601),r(74916),r(15306),r(41539),r(88674);var n=r(96486),i=r.n(n),a=r(99271),o=r(31636),s=r(93505),l=r(29564),c=(r(21249),r(89554),r(54747),r(82526),r(41817),r(32165),r(66992),r(78783),r(33948),r(69070),r(47941),r(57327),r(38880),r(49337),r(33321),r(85521)),u=r(7069),v=r(50186),d=r(34587),f=r(16770),p=r(85636);function h(t,e){var r=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),r.push.apply(r,n)}return r}function y(t){for(var e=1;e<arguments.length;e++){var r=null!=arguments[e]?arguments[e]:{};e%2?h(Object(r),!0).forEach((function(e){m(t,e,r[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(r)):h(Object(r)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(r,e))}))}return t}function m(t,e,r){return e in t?Object.defineProperty(t,e,{value:r,enumerable:!0,configurable:!0,writable:!0}):t[e]=r,t}function b(t){return b="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},b(t)}const g={name:"Reports",components:{TooltipHelpIcon:l.Z},mixins:[o.Jl],props:{bus:{type:Object,required:!0},runIds:{required:!0,validator:function(t){return"object"===b(t)||null===t}},reportFilter:{type:Object,required:!0}},data:function(){var t=(0,c.Z)(),e=(0,u.Z)(t,7),r=(0,u.Z)(t,31),n=[{label:"Today",date:[(0,v.Z)(),t]},{label:"Yesterday",date:[(0,d.Z)(),(0,f.Z)()]},{label:"Last 7 days",date:[e,t]},{label:"Last 31 days",date:[r,t]}];return{reportTypes:[{id:"new",label:"Number of outstanding reports",color:"red",icon:"mdi-arrow-up",getValue:this.getNewReports,cols:n.map((function(t){return y(y({},t),{},{value:null,loading:null})}))},{id:"resolved",label:"Number of resolved reports",color:"green",icon:"mdi-arrow-down",getValue:this.getResolvedReports,cols:n.map((function(t){return y(y({},t),{},{value:null,loading:null})}))}],activeReviewStatuses:[p.ReviewStatus.UNREVIEWED,p.ReviewStatus.CONFIRMED],resolvedReviewStatuses:[p.ReviewStatus.FALSE_POSITIVE,p.ReviewStatus.INTENTIONAL]}},activated:function(){var t=this;this.bus.$on("refresh",(function(){return t.fetchValues()}))},methods:{fetchValues:function(){this.reportTypes.forEach((function(t){return t.cols.forEach((function(e){return t.getValue(e,e.date)}))}))},getReportCount:function(t,e,r,n){t.loading="white",a.mv.getClient().getRunResultCount(e,r,n,(0,a.nC)((function(e){t.value=e.toNumber(),t.loading=null})))},getNewReports:function(t,e){var r=new p.ReportFilter(this.reportFilter);r.detectionStatus=null,r.reviewStatus=this.activeReviewStatuses,r.openReportsDate=this.getUnixTime(e[0]);var n=new p.CompareData({runIds:this.runIds,openReportsDate:this.getUnixTime(e[1]),diffType:p.DiffType.NEW});this.getReportCount(t,this.runIds,r,n)},getResolvedReports:function(t,e){var r=new p.ReportFilter(this.reportFilter);r.detectionStatus=null,r.date=new p.ReportDate({fixed:new p.DateInterval({after:this.getUnixTime(e[0]),before:this.getUnixTime(e[1])})}),this.getReportCount(t,this.runIds,r,null)}}};r(89943);var _=r(51900),C=r(43453),w=r.n(C),S=r(74811),x=r(53544),O=r(55136),R=r(19846),k=r(13047),D=r(90798),I=(0,_.Z)(g,(function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("v-container",{staticClass:"pa-0",attrs:{fluid:""}},[r("v-row",t._l(t.reportTypes,(function(e){return r("v-col",{key:e.label,attrs:{md:"12",lg:"6"}},[r("v-card",{attrs:{color:e.color,dark:""}},[r("v-card-title",{staticClass:"text-h4"},[r("v-icon",{staticClass:"mr-2"},[t._v("\n            "+t._s(e.icon)+"\n          ")]),t._v("\n          "+t._s(e.label)+"\n\n          "),r("tooltip-help-icon",{attrs:{color:"white"}},["new"===e.id?r("div",[t._v("\n              Shows the number of reports which were active in the last\n              "),r("i",[t._v("x")]),t._v(" days."),r("br"),r("br"),t._v(" "),r("b",[t._v("False positive")]),t._v(" and "),r("b",[t._v("Intentional")]),t._v(" reports are not\n              considered outstanding.\n            ")]):r("div",[t._v("\n              Shows the number of reports which were solved in the last\n              "),r("i",[t._v("x")]),t._v(" days."),r("br"),r("br"),t._v("\n\n              For now reports marked as "),r("b",[t._v("False positive")]),t._v(" or\n              "),r("b",[t._v("Intentional")]),t._v(" are not considered to be resolved by these\n              numbers. A report is marked as resolved only when it disspeared\n              from a storage."),r("br"),r("br")]),t._v(" "),r("div",[t._v("\n              The following filters don't affect these values:\n              "),r("ul",[r("li",[r("b",[t._v("Outstanding reports on a given date")]),t._v(" filter.")]),t._v(" "),r("li",[t._v("All filters in the "),r("b",[t._v("COMPARE TO")]),t._v(" section.")]),t._v(" "),r("li",[r("b",[t._v("Latest Review Status")]),t._v(" filter.")]),t._v(" "),r("li",[r("b",[t._v("Latest Detection Status")]),t._v(" filter.")])])])])],1),t._v(" "),r("v-row",t._l(e.cols,(function(n){return r("v-col",{key:n.label,attrs:{cols:12/e.cols.length}},[r("router-link",{staticClass:"text-decoration-none",attrs:{to:{name:"reports",query:Object.assign({},t.$router.currentRoute.query,{newcheck:void 0,"compared-to-open-reports-date":void 0},"new"===e.id?{"open-reports-date":t.dateTimeToStr(n.date[0]),"compared-to-open-reports-date":t.dateTimeToStr(n.date[1]),"diff-type":"New","review-status":["Confirmed bug","Unreviewed"]}:{"fixed-after":t.dateTimeToStr(n.date[0]),"fixed-before":t.dateTimeToStr(n.date[1])})}}},[r("v-card",{staticClass:"day-col text-center",attrs:{color:"transparent",loading:n.loading,flat:""}},[r("div",{staticClass:"text-h2"},[t._v("\n                  "+t._s(n.value)+"\n                ")]),t._v(" "),r("v-card-title",{staticClass:"justify-center"},[t._v("\n                  "+t._s(n.label)+"\n                ")])],1)],1)],1)})),1)],1)],1)})),1)],1)}),[],!1,null,"6ce34b56",null);const Z=I.exports;w()(I,{VCard:S.Z,VCardTitle:x.EB,VCol:O.Z,VContainer:R.Z,VIcon:k.Z,VRow:D.Z}),r(35666),r(68309),r(85827);var T=r(806),E=(r(43290),r(47297)),F=r(59523),V=r.n(F),j=E.tA.reactiveData;const P={name:"ComponentSeverityStatisticsChart",extends:E.by,mixins:[j,o.ri],props:{statistics:{type:Array,required:!0},loading:{type:Boolean,required:!0}},data:function(){var t=this,e=[p.Severity.CRITICAL,p.Severity.HIGH,p.Severity.MEDIUM,p.Severity.LOW,p.Severity.STYLE,p.Severity.UNSPECIFIED],r=e.map((function(e){return t.severityFromCodeToString(e)})),n=e.map((function(e){return t.severityFromCodeToColor(e)}));return{severities:e,options:{legend:{display:!0,position:"bottom"},responsive:!0,maintainAspectRatio:!1,plugins:{datalabels:{backgroundColor:n}}},chartData:{labels:r,datasets:[{data:[],backgroundColor:n,datalabels:{color:"white",borderColor:"white",borderRadius:25,borderWidth:2,font:{weight:"bold"}}}]}}},watch:{loading:function(){var t=this;this.loading||(this.chartData.datasets[0].data=this.statistics.reduce((function(e,r){return t.chartData.labels.forEach((function(t,n){e[n]+=r[t.toLowerCase()].count})),e}),new Array(this.chartData.labels.length).fill(0)),this.renderChart(this.chartData,this.options))}},mounted:function(){this.addPlugin(V()),this.renderChart(this.chartData,this.options)}},q=(0,_.Z)(P,void 0,void 0,!1,null,null,null).exports,N={name:"ComponentSeverityStatisticsTable",extends:s.n_,data:function(){return{headers:[{text:"",value:"data-table-expand"},{text:"Component",value:"component",align:"center"},{text:"Critical",value:"critical.count",align:"center"},{text:"High",value:"high.count",align:"center"},{text:"Medium",value:"medium.count",align:"center"},{text:"Low",value:"low.count",align:"center"},{text:"Style",value:"style.count",align:"center"},{text:"Unspecified",value:"unspecified.count",align:"center"},{text:"All reports",value:"reports.count",align:"center"}]}}};function A(t,e,r,n,i,a,o){try{var s=t[a](o),l=s.value}catch(t){return void r(t)}s.done?e(l):Promise.resolve(l).then(n,i)}r(46684);const L={name:"ComponentSeverityStatistics",components:{ComponentSeverityStatisticsChart:q,ComponentSeverityStatisticsTable:(0,_.Z)(N,void 0,void 0,!1,null,"601ebc50",null).exports,DetectionStatusIcon:T._8,ReportDiffCount:s.N8,SeverityIcon:T.jg,TooltipHelpIcon:l.Z},mixins:[s.U0,o.ri],data:function(){var t=["critical","high","medium","low","style","unspecified","reports"];return{DetectionStatus:p.DetectionStatus,Severity:p.Severity,totalColumns:t,fieldsToUpdate:t}},methods:{getComponentStatistics:function(t,e,r,n){var i=new p.ReportFilter(r);return i.severity=null,i.componentNames=[t.name],new Promise((function(t){return a.mv.getClient().getSeverityCounts(e,i,n,(0,a.nC)((function(e){return t(e)})))}))},initStatistics:function(t){this.statistics=t.map((function(t){return{component:t.name,value:t.value||t.description,reports:(0,s.qC)(void 0),critical:(0,s.qC)(void 0),high:(0,s.qC)(void 0),medium:(0,s.qC)(void 0),low:(0,s.qC)(void 0),style:(0,s.qC)(void 0),unspecified:(0,s.qC)(void 0)}}))},getStatistics:function(t,e,r,n){var i,a=this;return(i=regeneratorRuntime.mark((function i(){var o,l;return regeneratorRuntime.wrap((function(i){for(;;)switch(i.prev=i.next){case 0:return i.next=2,a.getComponentStatistics(t,e,r,n);case 2:return o=i.sent,l=Object.keys(o).reduce((function(t,e){return t+o[e].toNumber()}),0),i.abrupt("return",{component:t.name,value:t.value||t.description,reports:(0,s.qC)(l),critical:(0,s.qC)(o[p.Severity.CRITICAL]),high:(0,s.qC)(o[p.Severity.HIGH]),medium:(0,s.qC)(o[p.Severity.MEDIUM]),low:(0,s.qC)(o[p.Severity.LOW]),style:(0,s.qC)(o[p.Severity.STYLE]),unspecified:(0,s.qC)(o[p.Severity.UNSPECIFIED])});case 5:case"end":return i.stop()}}),i)})),function(){var t=this,e=arguments;return new Promise((function(r,n){var a=i.apply(t,e);function o(t){A(a,r,n,o,s,"next",t)}function s(t){A(a,r,n,o,s,"throw",t)}o(void 0)}))})()}}},M=L;var U=r(30281),$=r(74673),H=(0,_.Z)(M,(function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("v-container",{attrs:{fluid:""}},[r("v-row",[r("v-col",[r("v-card",{attrs:{flat:""}},[r("v-card-title",{staticClass:"justify-center"},[t._v("\n          Component statistics\n\n          "),r("tooltip-help-icon",[t._v("\n            This table shows component statistics per severity\n            levels."),r("br"),r("br"),t._v("\n\n            Each row can be expanded which will show a checker statistics\n            for the actual component."),r("br"),r("br"),t._v("\n\n            The following filters don't affect these values:\n            "),r("ul",[r("li",[r("b",[t._v("Severity")]),t._v(" filter.")]),t._v(" "),r("li",[r("b",[t._v("Source component")]),t._v(" filter.")])])])],1),t._v(" "),r("component-severity-statistics-table",{attrs:{items:t.statistics,loading:t.loading,filters:t.statisticsFilters,"total-columns":t.totalColumns},scopedSlots:t._u([t._l([["critical",t.Severity.CRITICAL],["high",t.Severity.HIGH],["medium",t.Severity.MEDIUM],["low",t.Severity.LOW],["style",t.Severity.STYLE],["unspecified",t.Severity.UNSPECIFIED]],(function(e){return{key:"header."+e[0]+".count",fn:function(n){var i=n.header;return[r("span",{key:e[0]},[r("severity-icon",{attrs:{status:e[1],size:16}}),t._v("\n              "+t._s(i.text)+"\n            ")],1)]}}})),t._l([["critical",t.Severity.CRITICAL],["high",t.Severity.HIGH],["medium",t.Severity.MEDIUM],["low",t.Severity.LOW],["style",t.Severity.STYLE],["unspecified",t.Severity.UNSPECIFIED]],(function(e){return{key:"item."+e[0]+".count",fn:function(n){var i=n.item;return[r("span",{key:e[0]},[i[e[0]].count?r("router-link",{attrs:{to:{name:"reports",query:Object.assign({},t.$router.currentRoute.query,i.$queryParams||{},{"source-component":i.component,severity:t.severityFromCodeToString(e[1])})}}},[t._v("\n                "+t._s(i[e[0]].count)+"\n              ")]):t._e(),t._v(" "),r("report-diff-count",{attrs:{"num-of-new-reports":i[e[0]].new,"num-of-resolved-reports":i[e[0]].resolved,"extra-query-params":{"source-component":i.component,severity:t.severityFromCodeToString(e[1])}}})],1)]}}})),{key:"header.reports.count",fn:function(e){var n=e.header;return[r("detection-status-icon",{attrs:{status:t.DetectionStatus.UNRESOLVED,size:16,left:""}}),t._v("\n            "+t._s(n.text)+"\n          ")]}}],null,!0)})],1)],1)],1),t._v(" "),r("v-row",[r("v-col",[r("v-card",{attrs:{flat:""}},[r("v-card-title",{staticClass:"justify-center"},[t._v("\n          Report severities\n\n          "),r("tooltip-help-icon",[t._v("\n            This pie chart shows the checker severity distribution in the\n            product."),r("br"),r("br"),t._v("\n\n            The following filters don't affect these values:\n            "),r("ul",[r("li",[r("b",[t._v("Severity")]),t._v(" filter.")]),t._v(" "),r("li",[r("b",[t._v("Source component")]),t._v(" filter.")])])])],1),t._v(" "),r("v-row",{attrs:{justify:"center"}},[r("v-overlay",{attrs:{value:t.loading,absolute:!0,opacity:.2}},[r("v-progress-circular",{attrs:{indeterminate:"",size:"64"}})],1)],1),t._v(" "),r("component-severity-statistics-chart",{attrs:{loading:t.loading,statistics:t.statistics}})],1)],1)],1)],1)}),[],!1,null,null,null);const W=H.exports;w()(H,{VCard:S.Z,VCardTitle:x.EB,VCol:O.Z,VContainer:R.Z,VOverlay:U.Z,VProgressCircular:$.Z,VRow:D.Z}),r(2707);const B={name:"FailedFilesDialog",data:function(){return{dialog:!1,loading:!1,failedFiles:{}}},computed:{files:function(){return Object.keys(this.failedFiles).sort((function(t,e){return t.localeCompare(e)}))}},watch:{dialog:function(){var t=this;this.loading=!0,a.mv.getClient().getFailedFiles(null,(0,a.nC)((function(e){t.failedFiles=e,t.loading=!1})))}}};var z=r(11880),Y=r(8857),G=r(95026),J=r(89674),K=r(16151),Q=(0,_.Z)(B,(function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("v-dialog",{attrs:{"content-class":"documentation-dialog","max-width":"80%",scrollable:""},scopedSlots:t._u([{key:"activator",fn:function(e){var r=e.on;return[t._t("default",null,{on:r})]}}],null,!0),model:{value:t.dialog,callback:function(e){t.dialog=e},expression:"dialog"}},[t._v(" "),r("v-card",[r("v-card-title",{staticClass:"headline primary white--text",attrs:{"primary-title":""}},[t._v("\n      Failed files\n\n      "),r("v-spacer"),t._v(" "),r("v-btn",{staticClass:"close-btn",attrs:{icon:"",dark:""},on:{click:function(e){t.dialog=!1}}},[r("v-icon",[t._v("mdi-close")])],1)],1),t._v(" "),r("v-card-text",{staticClass:"pa-0"},[r("v-card",{attrs:{loading:t.loading,flat:""}},[r("v-container",[r("v-simple-table",{scopedSlots:t._u([{key:"default",fn:function(){return[r("thead",[r("tr",[r("th",{staticClass:"text-left"},[t._v("\n                    File path\n                  ")]),t._v(" "),r("th",{staticClass:"text-left"},[t._v("\n                    Failed to analyze in these runs\n                  ")])])]),t._v(" "),r("tbody",t._l(t.files,(function(e){return r("tr",{key:e},[r("td",[t._v("\n                    "+t._s(e)+"\n                  ")]),t._v(" "),r("td",t._l(t.failedFiles[e],(function(e){return r("v-chip",{key:e.runName,attrs:{color:"#878d96",outlined:"",small:""}},[t._v("\n                      "+t._s(e.runName)+"\n                    ")])})),1)])})),0)]},proxy:!0}])})],1)],1)],1)],1)],1)}),[],!1,null,null,null);const X=Q.exports;w()(Q,{VBtn:z.Z,VCard:S.Z,VCardText:x.ZB,VCardTitle:x.EB,VChip:Y.Z,VContainer:R.Z,VDialog:G.Z,VIcon:k.Z,VSimpleTable:J.Z,VSpacer:K.Z}),r(65069),r(47042),r(83710),r(92222),r(32023),r(79753),r(91038);var tt=r(67090),et=r(36961),rt=r(4135),nt=r(54559),it=r(10876),at=r(29807),ot=r(61532);function st(t,e,r,n,i,a,o){try{var s=t[a](o),l=s.value}catch(t){return void r(t)}s.done?e(l):Promise.resolve(l).then(n,i)}function lt(t,e){var r=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),r.push.apply(r,n)}return r}function ct(t){for(var e=1;e<arguments.length;e++){var r=null!=arguments[e]?arguments[e]:{};e%2?lt(Object(r),!0).forEach((function(e){ut(t,e,r[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(r)):lt(Object(r)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(r,e))}))}return t}function ut(t,e,r){return e in t?Object.defineProperty(t,e,{value:r,enumerable:!0,configurable:!0,writable:!0}):t[e]=r,t}function vt(t){return function(t){if(Array.isArray(t))return dt(t)}(t)||function(t){if("undefined"!=typeof Symbol&&null!=t[Symbol.iterator]||null!=t["@@iterator"])return Array.from(t)}(t)||function(t,e){if(t){if("string"==typeof t)return dt(t,e);var r=Object.prototype.toString.call(t).slice(8,-1);return"Object"===r&&t.constructor&&(r=t.constructor.name),"Map"===r||"Set"===r?Array.from(t):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?dt(t,e):void 0}}(t)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function dt(t,e){(null==e||e>t.length)&&(e=t.length);for(var r=0,n=new Array(e);r<e;r++)n[r]=t[r];return n}var ft=E.tA.reactiveData;const pt={name:"OutstandingReportsChart",extends:E.x1,mixins:[o.Jl,ft,o.ri],props:{bus:{type:Object,required:!0},getStatisticsFilters:{type:Function,required:!0},interval:{type:String,required:!0},resolution:{type:String,required:!0}},data:function(){var t=this;return{dates:[],options:{legend:{display:!0},responsive:!0,maintainAspectRatio:!1,tooltips:{mode:"index",callbacks:{footer:function(t,e){var r=t.reduce((function(t,r){return t+e.datasets[r.datasetIndex].data[r.index]}),0);return"Total: ".concat(r)}},intersect:!1},hover:{mode:"nearest",intersect:!0},scales:{xAxes:[{ticks:{padding:10}}]}},chartData:{labels:[],datasets:vt(Object.keys(p.Severity).reverse().map((function(e){var r=p.Severity[e],n=t.severityFromCodeToColor(r);return{type:"line",label:t.severityFromCodeToString(r),backgroundColor:n,borderColor:n,borderWidth:3,fill:!1,pointRadius:5,pointHoverRadius:10,datalabels:{backgroundColor:n,color:"white",borderRadius:4,font:{weight:"bold"}},data:[]}})))}}},watch:{interval:{handler:i().debounce((function(){var t=this.dates.length,e=parseInt(this.interval);if(this.setChartData(),e>t){var r=this.dates.slice(t);this.fetchData(r)}}),500)},resolution:function(){this.setChartData(),this.fetchData(this.dates)}},created:function(){this.setChartData()},mounted:function(){this.addPlugin(V()),this.renderChart(this.chartData,this.options)},activated:function(){var t=this;this.bus.$on("refresh",(function(){return t.fetchData(t.dates)}))},methods:{setChartData:function(){var t=this,e=parseInt(this.interval);if(!(isNaN(e)||e<=0)){var r="yyyy. MMM. dd";if("days"===this.resolution){var n=(0,c.Z)();this.dates=vt(new Array(e).keys()).map((function(t){return(0,u.Z)(n,t)}))}else if("weeks"===this.resolution){var i=(0,tt.Z)(new Date,{weekStartsOn:1});this.dates=vt(new Array(e).keys()).map((function(t){return(0,et.Z)(i,t)}))}else if("months"===this.resolution){var a=(0,rt.Z)(new Date);this.dates=vt(new Array(e).keys()).map((function(t){return(0,nt.Z)(a,t)})),r="yyyy. MMM"}else if("years"===this.resolution){var o=(0,it.Z)(new Date);this.dates=vt(new Array(e).keys()).map((function(t){return(0,at.Z)(o,t)})),r="yyyy"}this.chartData.labels=vt(this.dates).reverse().map((function(e,n){var i=(0,ot.Z)(e,r);return n===t.dates.length-1?"".concat(i," (Current)"):i})),this.chartData.datasets.forEach((function(e){t.dates.length>e.data.length?e.data=[].concat(vt(new Array(t.dates.length-e.data.length).fill(null)),vt(e.data)):e.data=e.data.slice(e.data.length-t.dates.length,e.data.length)})),this.chartData=ct({},this.chartData)}},fetchData:function(t){var e=this;this.dates.forEach(function(){var r,n=(r=regeneratorRuntime.mark((function r(n,i){var a,o;return regeneratorRuntime.wrap((function(r){for(;;)switch(r.prev=r.next){case 0:if(t.includes(n)){r.next=2;break}return r.abrupt("return");case 2:return r.next=4,e.fetchOutstandingReports(n);case 4:a=r.sent,o=e.chartData.datasets,Object.keys(p.Severity).reverse().forEach((function(t,e){var r,n=p.Severity[t],s=(null===(r=a[n])||void 0===r?void 0:r.toNumber())||0,l=o[e].data;l[l.length-1-i]=s})),e.chartData=ct({},e.chartData);case 8:case"end":return r.stop()}}),r)})),function(){var t=this,e=arguments;return new Promise((function(n,i){var a=r.apply(t,e);function o(t){st(a,n,i,o,s,"next",t)}function s(t){st(a,n,i,o,s,"throw",t)}o(void 0)}))});return function(t,e){return n.apply(this,arguments)}}())},fetchOutstandingReports:function(t){var e=this.getStatisticsFilters(),r=e.runIds,n=e.reportFilter,i=new p.ReportFilter(n);return i.openReportsDate=this.getUnixTime(t),i.detectionStatus=null,new Promise((function(t){a.mv.getClient().getSeverityCounts(r,i,null,(0,a.nC)((function(e){return t(e)})))}))}}},ht=(0,_.Z)(pt,void 0,void 0,!1,null,null,null).exports;function yt(t,e,r,n,i,a,o){try{var s=t[a](o),l=s.value}catch(t){return void r(t)}s.done?e(l):Promise.resolve(l).then(n,i)}const mt={name:"SingleLineWidget",components:{TooltipHelpIcon:l.Z},props:{icon:{type:String,required:!0},color:{type:String,required:!0},label:{type:String,required:!0},helpMessage:{type:String,default:null},bus:{type:Object,required:!0},getValue:{type:Function,required:!0}},data:function(){return{loading:!1,value:null}},activated:function(){var t=this;this.bus.$on("refresh",(function(){return t.fetchValue()}))},methods:{fetchValue:function(){var t,e=this;return(t=regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return e.loading=!0,t.next=3,e.getValue();case 3:e.value=t.sent,e.loading=!1;case 5:case"end":return t.stop()}}),t)})),function(){var e=this,r=arguments;return new Promise((function(n,i){var a=t.apply(e,r);function o(t){yt(a,n,i,o,s,"next",t)}function s(t){yt(a,n,i,o,s,"throw",t)}o(void 0)}))})()}}};r(22351);var bt=r(35605),gt=(0,_.Z)(mt,(function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("v-card",{attrs:{loading:t.loading,flat:""}},[r("v-container",[r("v-row",[r("v-col",{attrs:{cols:"auto"}},[r("v-avatar",{attrs:{color:t.color,size:"64",tile:""}},[r("v-icon",{attrs:{dark:"",size:"48"}},[t._v("\n            "+t._s(t.icon)+"\n          ")])],1)],1),t._v(" "),r("v-col",{staticClass:"text-center"},[r("div",{staticClass:"subtitle grey--text text-uppercase"},[t._v("\n          "+t._s(t.label)+"\n\n          "),r("tooltip-help-icon",[t._t("help")],2)],1),t._v(" "),r("div",{staticClass:"text-h3 font-weight-bold"},[t._t("value",(function(){return[t._v("\n            "+t._s(t.value)+"\n          ")]}),{value:t.value}),t._v(" "),t._t("append-value")],2)])],1)],1)],1)}),[],!1,null,"24a4abfb",null);const _t=gt.exports;w()(gt,{VAvatar:bt.Z,VCard:S.Z,VCol:O.Z,VContainer:R.Z,VIcon:k.Z,VRow:D.Z});const Ct={name:"Overview",components:{ComponentSeverityStatistics:W,FailedFilesDialog:X,OutstandingReportsChart:ht,Reports:Z,SingleLineWidget:_t,TooltipHelpIcon:l.Z},mixins:[s.HB,o.Jl],data:function(){var t=["days","weeks","months","years"],e=t[0],r=this.$route.query.interval;this.validateIntervalValue(r)&&(r="7");var n=this.$route.query.resolution;return n&&t.includes(n)||(n=e),{intervalError:null,interval:r,resolutions:t,resolution:n}},methods:{validateIntervalValue:function(t){return!t||isNaN(parseInt(t))?"Number is required!":parseInt(t)>31?"Interval value should between 1-31!":null},setInterval:i().debounce((function(t){this.intervalError=this.validateIntervalValue(t),this.intervalError||(this.interval=t,this.updateUrl(),this.intervalError=null)}),300),setResolution:function(t){this.resolution=t,this.updateUrl()},updateUrl:function(){var t=Object.assign({},this.$route.query,{interval:this.interval,resolution:this.resolution});this.$router.replace({query:t}).catch((function(){}))},getNumberOfReports:function(t,e,r){return new Promise((function(n){a.mv.getClient().getRunResultCount(t,e,r,(0,a.nC)((function(t){n(t.toNumber())})))}))},getNumberOfFailedFiles:function(){var t=this;return new Promise((function(e){a.mv.getClient().getFailedFilesCount(t.runIds,(0,a.nC)((function(t){e(t)})))}))},getNumberOfActiveCheckers:function(){var t=this.getStatisticsFilters(),e=t.runIds,r=t.reportFilter,n=t.cmpData;return new Promise((function(t){a.mv.getClient().getCheckerCounts(e,r,n,null,0,(0,a.nC)((function(e){t(e.length)})))}))}}};r(42671);var wt=r(58119),St=r(64316),xt=r(14462),Ot=(0,_.Z)(Ct,(function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("v-container",{attrs:{fluid:""}},[r("reports",{attrs:{bus:t.bus,"run-ids":t.runIds,"report-filter":t.reportFilter}}),t._v(" "),r("v-row",[r("v-col",[r("single-line-widget",{attrs:{icon:"mdi-close",color:"red",label:"Number of failed files",bus:t.bus,"get-value":t.getNumberOfFailedFiles},scopedSlots:t._u([{key:"help",fn:function(){return[t._v("\n          Number of failed files in the current product."),r("br"),r("br"),t._v("\n          Only the Run filter will affect this value.\n        ")]},proxy:!0},{key:"value",fn:function(e){var n=e.value;return[r("failed-files-dialog",{scopedSlots:t._u([{key:"default",fn:function(e){var i=e.on;return[r("span",t._g({staticClass:"num-of-failed-files"},i),[t._v("\n                "+t._s(n)+"\n              ")])]}}],null,!0)})]}}])})],1),t._v(" "),r("v-col",[r("single-line-widget",{attrs:{icon:"mdi-card-account-details",color:"grey",label:"Number of checkers reporting faults",bus:t.bus,"get-value":t.getNumberOfActiveCheckers},scopedSlots:t._u([{key:"help",fn:function(){return[t._v("\n          Number of checkers which found some report in the current\n          product."),r("br"),r("br"),t._v("\n\n          Every filter will affect this value.\n        ")]},proxy:!0}])})],1)],1),t._v(" "),r("v-row",{staticClass:"my-4"},[r("v-col",[r("v-card",{attrs:{flat:""}},[r("v-card-title",{staticClass:"justify-center"},[t._v("\n          Number of outstanding reports\n\n          "),r("tooltip-help-icon",[t._v("\n            Shows the number of reports which were active in the last\n            "),r("i",[t._v("x")]),t._v(" months/days."),r("br"),r("br"),t._v("\n\n            The following filters don't affect these values:\n            "),r("ul",[r("li",[r("b",[t._v("Outstanding reports on a given date")]),t._v(" filter.")]),t._v(" "),r("li",[t._v("All filters in the "),r("b",[t._v("COMPARE TO")]),t._v(" section.")]),t._v(" "),r("li",[r("b",[t._v("Latest Review Status")]),t._v(" filter.")]),t._v(" "),r("li",[r("b",[t._v("Latest Detection Status")]),t._v(" filter.")])])])],1),t._v(" "),r("v-form",{ref:"form",staticClass:"interval-selector"},[r("v-text-field",{staticClass:"interval align-center",attrs:{value:t.interval,type:"number","hide-details":"",dense:"",solo:""},on:{input:t.setInterval},scopedSlots:t._u([{key:"prepend",fn:function(){return[t._v("\n              Last\n            ")]},proxy:!0},{key:"append-outer",fn:function(){return[r("v-select",{staticClass:"resolution",attrs:{value:t.resolution,items:t.resolutions,label:"Resolution","hide-details":"",dense:"",solo:""},on:{input:t.setResolution}})]},proxy:!0}])}),t._v(" "),t.intervalError?r("div",{staticClass:"red--text"},[t._v("\n            "+t._s(t.intervalError)+"\n          ")]):t._e()],1),t._v(" "),r("outstanding-reports-chart",{attrs:{bus:t.bus,"get-statistics-filters":t.getStatisticsFilters,interval:t.interval,resolution:t.resolution,styles:{height:"400px",position:"relative"}}})],1)],1)],1),t._v(" "),r("v-row",[r("v-col",[r("component-severity-statistics",{attrs:{bus:t.bus,namespace:t.namespace}})],1)],1)],1)}),[],!1,null,"6a6c9fd7",null);const Rt=Ot.exports;w()(Ot,{VCard:S.Z,VCardTitle:x.EB,VCol:O.Z,VContainer:R.Z,VForm:wt.Z,VRow:D.Z,VSelect:St.Z,VTextField:xt.Z})}}]);