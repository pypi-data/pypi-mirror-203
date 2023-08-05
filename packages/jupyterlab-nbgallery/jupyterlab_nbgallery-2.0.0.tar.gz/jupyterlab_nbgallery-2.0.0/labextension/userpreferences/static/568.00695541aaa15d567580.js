"use strict";(self.webpackChunk_jupyterlab_nbgallery_userpreferences=self.webpackChunk_jupyterlab_nbgallery_userpreferences||[]).push([[568],{568:(e,r,t)=>{t.r(r),t.d(r,{default:()=>p});var a=t(344),s=t(33),n=t(832),l=t(820),o=t(142),i=t(569),c=t.n(i);const u={id:"@jupyterlab-nbgallery/userpreferences",autoStart:!0,requires:[a.IMainMenu],activate:function(e,r){new d(e,r).startup()}};class d{constructor(e,r){this.app=e,this.mainMenu=r,this.settings=l.ServerConnection.makeSettings()}async startup(){const e=o.URLExt.join(this.settings.baseUrl,"jupyterlab_nbgallery","environment");let r=this;await c().ajax({method:"GET",headers:{Accept:"application/json"},url:e,cache:!1,xhrFields:{withCredentials:!0},success:function(e){r.gallery_url=new URL(e.NBGALLERY_URL)}}),this.gallery_preferences_url=o.URLExt.join(this.gallery_url.origin,"preferences"),this.jupyter_preferences_url=o.URLExt.join(this.settings.baseUrl,"jupyterlab_nbgallery","preferences"),this.gallery_menu=this.buildMenus(),this.mainMenu.addMenu(this.gallery_menu,{rank:50})}buildMenus(){console.log("Building Menus");const{commands:e}=this.app;var r;e.addCommand("preferences-upload",{label:"Save Preferences to the Gallery",isEnabled:()=>!0,isVisible:()=>!0,execute:()=>{this.uploadPreferences()}}),e.addCommand("preferences-download",{label:"Download Preferences from the Gallery",isEnabled:()=>!0,isVisible:()=>!0,execute:()=>{this.downloadPreferences()}}),e.addCommand("preferences-reset",{label:"Reset Preferences to Defaults",isEnabled:()=>!0,isVisible:()=>!0,execute:()=>{this.resetPreferences()}}),r=null;var t,a=this.mainMenu.menus;for(let e=0;e<a.length;e++)"jupyterlab_nbgallery-gallery"==a[e].id&&(r=a[e]);return null==r&&((r=new n.Menu({commands:e})).title.label="Gallery",r.id="jupyterlab_nbgallery-gallery"),(t=new n.Menu({commands:e})).title.label="Jupyter Preferences",t.addItem({command:"preferences-upload"}),t.addItem({command:"preferences-download"}),t.addItem({command:"preferences-reset"}),r.addItem({type:"separator"}),r.addItem({type:"submenu",submenu:t}),r}async uploadPreferences(){let e=await c().ajax({method:"GET",url:this.jupyter_preferences_url,cache:!1,headers:{Accept:"application/json"},xhrFields:{withCredentials:!0}});await c().ajax({method:"POST",url:this.gallery_preferences_url,data:{lab_preferences:JSON.stringify(e)},headers:{Accept:"application/json"},xhrFields:{withCredentials:!0},error:function(){(0,s.showErrorMessage)("Error Uploading Preferences","An error occured saving your preferences to NBGallery.  Please try again later or contact the site adminsitrators.")}})}async downloadPreferences(){let e=await c().ajax({method:"GET",url:this.gallery_preferences_url,cache:!1,headers:{Accept:"application/json"},xhrFields:{withCredentials:!0}});c().ajax({method:"POST",url:this.jupyter_preferences_url,data:e.lab_preferences,xhrFields:{withCredentials:!0},cache:!1,complete:function(e,r){"success"==r||"parsererror"==r?(0,s.showDialog)({title:"Reload may be required",body:"For all settings to take affect, you may need to reload the Jupyter interface",buttons:[s.Dialog.okButton()]}):(0,s.showErrorMessage)("Error Downloading Preferences","An error occured while attempting to update your preferences in Jupyter.  Please try again later.")}})}async resetPreferences(){let e=this;(0,s.showDialog)({title:"Reset User Preferences?",body:"This will delete ALL local preferences you have customized in your image restoring JupyterLab to the defaults.  Your preferences saved to the gallery will not be impacted.  Proceed?",buttons:[s.Dialog.cancelButton(),s.Dialog.warnButton()]}).then((r=>{r.button.accept&&c().ajax({method:"DELETE",url:e.jupyter_preferences_url,xhrFields:{withCredentials:!0},cache:!1,complete:function(e,r){"success"==r||"parsererror"==r?(0,s.showDialog)({title:"Reload may be required",body:"For all default settings to take affect, you may need to reload the Jupyter interface",buttons:[s.Dialog.okButton()]}):(0,s.showErrorMessage)("Error Resetting Preferences","An error occured while attempting to reset your preferences in Jupyter.  Please try again later.")}})}))}}const p=u}}]);