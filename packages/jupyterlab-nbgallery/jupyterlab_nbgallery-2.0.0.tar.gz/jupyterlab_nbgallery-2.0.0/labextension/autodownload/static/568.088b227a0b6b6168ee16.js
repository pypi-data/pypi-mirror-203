"use strict";(self.webpackChunk_jupyterlab_nbgallery_autodownload=self.webpackChunk_jupyterlab_nbgallery_autodownload||[]).push([[568],{568:(e,o,t)=>{t.r(o),t.d(o,{default:()=>s});var n=t(38),a=t(142),c=t(569),r=t.n(c);const s={id:"@jupyterlab-nbgallery/autodownload",autoStart:!0,requires:[n.ISettingRegistry],activate:async(e,o)=>{let t="",n=0,c=!1;function s(){return a.PageConfig.getBaseUrl()}function l(e,o,t){r().ajax({method:"GET",headers:{Accept:"application/json"},url:e,cache:!1,xhrFields:{withCredentials:!0},success:function(e){!async function(e,o,t){r().ajax({url:s()+"post/"+e+"/"+encodeURIComponent(o)+".ipynb",type:"POST",success:function(){},error:function(e){console.error("Failed upload: "+o)},data:JSON.stringify({type:"notebook",content:JSON.parse(t)})})}(o,t,e)}})}function i(e,o,t){r().ajax({method:"GET",url:s()+"api/contents/"+encodeURIComponent(e),cache:!1,xhrFields:{withCredentials:!0},success:function(e){},error:function(n){console.info("Downloading notebooks to "+e),r().ajax({method:"POST",url:s()+"post/"+encodeURIComponent(e),data:JSON.stringify({type:"directory"}),cache:!1,success:function(n){r().ajax({method:"GET",headers:{Accept:"application/json"},url:o+t,cache:!1,xhrFields:{withCredentials:!0},success:function(t){let n;for(n in t){var a=t[n];l(o+"/notebooks/"+a.uuid+"/download?clickstream=false",e,a.title.replace(/\//g,"⁄"))}}})}})}})}Promise.all([e.restored,o.load("@jupyterlab-nbgallery/autodownload:autodownload")]).then((([,e])=>{try{!function(e){r().ajax({method:"GET",headers:{Accept:"application/json"},url:s()+"jupyterlab_nbgallery/environment",cache:!1,xhrFields:{withCredentials:!0},success:function(o){t=o.NBGALLERY_URL,n=o.NBGALLERY_ENABLE_AUTODOWNLOAD,c=e.get("enabled").composite,console.info("Auto Downloading Notebooks"),(1==n||c)&&(i("Starred",t,"/notebooks/stars"),i("Recently Executed",t,"/notebooks/recently_executed"))}})}(e)}catch(e){console.error(`Problem downloading notebooks \n ${e}`)}}))}}}}]);