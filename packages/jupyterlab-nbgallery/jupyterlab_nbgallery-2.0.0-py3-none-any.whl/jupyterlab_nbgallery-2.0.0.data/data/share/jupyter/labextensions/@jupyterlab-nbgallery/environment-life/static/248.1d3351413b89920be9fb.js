"use strict";(self.webpackChunk_jupyterlab_nbgallery_environment_life=self.webpackChunk_jupyterlab_nbgallery_environment_life||[]).push([[248],{248:(e,t,n)=>{n.r(t),n.d(t,{default:()=>s});var r=n(832),i=n(583),o=n(142),a=n(820);const s={id:"@jupyterlab-nbgallery/environment-life",autoStart:!0,requires:[i.IStatusBar],activate:async(e,t)=>{let n="";try{const e=await async function(e="",t={}){const n=a.ServerConnection.makeSettings(),r=o.URLExt.join(n.baseUrl,"jupyterlab_nbgallery",e);let i;try{i=await a.ServerConnection.makeRequest(r,t,n)}catch(e){throw new a.ServerConnection.NetworkError(e)}const s=await i.json();if(!i.ok)throw new a.ServerConnection.ResponseError(i,s.message);return s}("expiration");n=e.NBGALLERY_TERMINATION_TIME,function(){if(console.log(`termination Time: ${n}`),n&&n.length>0){let e=new Date(n+" UTC");const r=new l;r.node.textContent="Expires: "+e.toLocaleString(),t.registerStatusItem("bench-expiration",{align:"right",item:r})}}()}catch(e){console.error(`ERROR on get /jupyter_nbgallery/environment.\n ${e}`)}}};class l extends r.Widget{constructor(){super(),this.addClass("jp-expiration-widget"),this.id="environment_expires",this.title.label="Jupyter Environment Expires"}}}}]);