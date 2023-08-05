"use strict";(self.webpackChunk_jupyterlab_nbgallery_instrumentation=self.webpackChunk_jupyterlab_nbgallery_instrumentation||[]).push([[701],{701:(e,t,r)=>{r.r(t),r.d(t,{Md5:()=>s,Md5FileHasher:()=>a,ParallelHasher:()=>h});class s{constructor(){this._dataLength=0,this._bufferLength=0,this._state=new Int32Array(4),this._buffer=new ArrayBuffer(68),this._buffer8=new Uint8Array(this._buffer,0,68),this._buffer32=new Uint32Array(this._buffer,0,17),this.start()}static hashStr(e,t=!1){return this.onePassHasher.start().appendStr(e).end(t)}static hashAsciiStr(e,t=!1){return this.onePassHasher.start().appendAsciiStr(e).end(t)}static _hex(e){const t=s.hexChars,r=s.hexOut;let a,h,i,n;for(n=0;n<4;n+=1)for(h=8*n,a=e[n],i=0;i<8;i+=2)r[h+1+i]=t.charAt(15&a),a>>>=4,r[h+0+i]=t.charAt(15&a),a>>>=4;return r.join("")}static _md5cycle(e,t){let r=e[0],s=e[1],a=e[2],h=e[3];r+=(s&a|~s&h)+t[0]-680876936|0,r=(r<<7|r>>>25)+s|0,h+=(r&s|~r&a)+t[1]-389564586|0,h=(h<<12|h>>>20)+r|0,a+=(h&r|~h&s)+t[2]+606105819|0,a=(a<<17|a>>>15)+h|0,s+=(a&h|~a&r)+t[3]-1044525330|0,s=(s<<22|s>>>10)+a|0,r+=(s&a|~s&h)+t[4]-176418897|0,r=(r<<7|r>>>25)+s|0,h+=(r&s|~r&a)+t[5]+1200080426|0,h=(h<<12|h>>>20)+r|0,a+=(h&r|~h&s)+t[6]-1473231341|0,a=(a<<17|a>>>15)+h|0,s+=(a&h|~a&r)+t[7]-45705983|0,s=(s<<22|s>>>10)+a|0,r+=(s&a|~s&h)+t[8]+1770035416|0,r=(r<<7|r>>>25)+s|0,h+=(r&s|~r&a)+t[9]-1958414417|0,h=(h<<12|h>>>20)+r|0,a+=(h&r|~h&s)+t[10]-42063|0,a=(a<<17|a>>>15)+h|0,s+=(a&h|~a&r)+t[11]-1990404162|0,s=(s<<22|s>>>10)+a|0,r+=(s&a|~s&h)+t[12]+1804603682|0,r=(r<<7|r>>>25)+s|0,h+=(r&s|~r&a)+t[13]-40341101|0,h=(h<<12|h>>>20)+r|0,a+=(h&r|~h&s)+t[14]-1502002290|0,a=(a<<17|a>>>15)+h|0,s+=(a&h|~a&r)+t[15]+1236535329|0,s=(s<<22|s>>>10)+a|0,r+=(s&h|a&~h)+t[1]-165796510|0,r=(r<<5|r>>>27)+s|0,h+=(r&a|s&~a)+t[6]-1069501632|0,h=(h<<9|h>>>23)+r|0,a+=(h&s|r&~s)+t[11]+643717713|0,a=(a<<14|a>>>18)+h|0,s+=(a&r|h&~r)+t[0]-373897302|0,s=(s<<20|s>>>12)+a|0,r+=(s&h|a&~h)+t[5]-701558691|0,r=(r<<5|r>>>27)+s|0,h+=(r&a|s&~a)+t[10]+38016083|0,h=(h<<9|h>>>23)+r|0,a+=(h&s|r&~s)+t[15]-660478335|0,a=(a<<14|a>>>18)+h|0,s+=(a&r|h&~r)+t[4]-405537848|0,s=(s<<20|s>>>12)+a|0,r+=(s&h|a&~h)+t[9]+568446438|0,r=(r<<5|r>>>27)+s|0,h+=(r&a|s&~a)+t[14]-1019803690|0,h=(h<<9|h>>>23)+r|0,a+=(h&s|r&~s)+t[3]-187363961|0,a=(a<<14|a>>>18)+h|0,s+=(a&r|h&~r)+t[8]+1163531501|0,s=(s<<20|s>>>12)+a|0,r+=(s&h|a&~h)+t[13]-1444681467|0,r=(r<<5|r>>>27)+s|0,h+=(r&a|s&~a)+t[2]-51403784|0,h=(h<<9|h>>>23)+r|0,a+=(h&s|r&~s)+t[7]+1735328473|0,a=(a<<14|a>>>18)+h|0,s+=(a&r|h&~r)+t[12]-1926607734|0,s=(s<<20|s>>>12)+a|0,r+=(s^a^h)+t[5]-378558|0,r=(r<<4|r>>>28)+s|0,h+=(r^s^a)+t[8]-2022574463|0,h=(h<<11|h>>>21)+r|0,a+=(h^r^s)+t[11]+1839030562|0,a=(a<<16|a>>>16)+h|0,s+=(a^h^r)+t[14]-35309556|0,s=(s<<23|s>>>9)+a|0,r+=(s^a^h)+t[1]-1530992060|0,r=(r<<4|r>>>28)+s|0,h+=(r^s^a)+t[4]+1272893353|0,h=(h<<11|h>>>21)+r|0,a+=(h^r^s)+t[7]-155497632|0,a=(a<<16|a>>>16)+h|0,s+=(a^h^r)+t[10]-1094730640|0,s=(s<<23|s>>>9)+a|0,r+=(s^a^h)+t[13]+681279174|0,r=(r<<4|r>>>28)+s|0,h+=(r^s^a)+t[0]-358537222|0,h=(h<<11|h>>>21)+r|0,a+=(h^r^s)+t[3]-722521979|0,a=(a<<16|a>>>16)+h|0,s+=(a^h^r)+t[6]+76029189|0,s=(s<<23|s>>>9)+a|0,r+=(s^a^h)+t[9]-640364487|0,r=(r<<4|r>>>28)+s|0,h+=(r^s^a)+t[12]-421815835|0,h=(h<<11|h>>>21)+r|0,a+=(h^r^s)+t[15]+530742520|0,a=(a<<16|a>>>16)+h|0,s+=(a^h^r)+t[2]-995338651|0,s=(s<<23|s>>>9)+a|0,r+=(a^(s|~h))+t[0]-198630844|0,r=(r<<6|r>>>26)+s|0,h+=(s^(r|~a))+t[7]+1126891415|0,h=(h<<10|h>>>22)+r|0,a+=(r^(h|~s))+t[14]-1416354905|0,a=(a<<15|a>>>17)+h|0,s+=(h^(a|~r))+t[5]-57434055|0,s=(s<<21|s>>>11)+a|0,r+=(a^(s|~h))+t[12]+1700485571|0,r=(r<<6|r>>>26)+s|0,h+=(s^(r|~a))+t[3]-1894986606|0,h=(h<<10|h>>>22)+r|0,a+=(r^(h|~s))+t[10]-1051523|0,a=(a<<15|a>>>17)+h|0,s+=(h^(a|~r))+t[1]-2054922799|0,s=(s<<21|s>>>11)+a|0,r+=(a^(s|~h))+t[8]+1873313359|0,r=(r<<6|r>>>26)+s|0,h+=(s^(r|~a))+t[15]-30611744|0,h=(h<<10|h>>>22)+r|0,a+=(r^(h|~s))+t[6]-1560198380|0,a=(a<<15|a>>>17)+h|0,s+=(h^(a|~r))+t[13]+1309151649|0,s=(s<<21|s>>>11)+a|0,r+=(a^(s|~h))+t[4]-145523070|0,r=(r<<6|r>>>26)+s|0,h+=(s^(r|~a))+t[11]-1120210379|0,h=(h<<10|h>>>22)+r|0,a+=(r^(h|~s))+t[2]+718787259|0,a=(a<<15|a>>>17)+h|0,s+=(h^(a|~r))+t[9]-343485551|0,s=(s<<21|s>>>11)+a|0,e[0]=r+e[0]|0,e[1]=s+e[1]|0,e[2]=a+e[2]|0,e[3]=h+e[3]|0}start(){return this._dataLength=0,this._bufferLength=0,this._state.set(s.stateIdentity),this}appendStr(e){const t=this._buffer8,r=this._buffer32;let a,h,i=this._bufferLength;for(h=0;h<e.length;h+=1){if(a=e.charCodeAt(h),a<128)t[i++]=a;else if(a<2048)t[i++]=192+(a>>>6),t[i++]=63&a|128;else if(a<55296||a>56319)t[i++]=224+(a>>>12),t[i++]=a>>>6&63|128,t[i++]=63&a|128;else{if(a=1024*(a-55296)+(e.charCodeAt(++h)-56320)+65536,a>1114111)throw new Error("Unicode standard supports code points up to U+10FFFF");t[i++]=240+(a>>>18),t[i++]=a>>>12&63|128,t[i++]=a>>>6&63|128,t[i++]=63&a|128}i>=64&&(this._dataLength+=64,s._md5cycle(this._state,r),i-=64,r[0]=r[16])}return this._bufferLength=i,this}appendAsciiStr(e){const t=this._buffer8,r=this._buffer32;let a,h=this._bufferLength,i=0;for(;;){for(a=Math.min(e.length-i,64-h);a--;)t[h++]=e.charCodeAt(i++);if(h<64)break;this._dataLength+=64,s._md5cycle(this._state,r),h=0}return this._bufferLength=h,this}appendByteArray(e){const t=this._buffer8,r=this._buffer32;let a,h=this._bufferLength,i=0;for(;;){for(a=Math.min(e.length-i,64-h);a--;)t[h++]=e[i++];if(h<64)break;this._dataLength+=64,s._md5cycle(this._state,r),h=0}return this._bufferLength=h,this}getState(){const e=this._state;return{buffer:String.fromCharCode.apply(null,Array.from(this._buffer8)),buflen:this._bufferLength,length:this._dataLength,state:[e[0],e[1],e[2],e[3]]}}setState(e){const t=e.buffer,r=e.state,s=this._state;let a;for(this._dataLength=e.length,this._bufferLength=e.buflen,s[0]=r[0],s[1]=r[1],s[2]=r[2],s[3]=r[3],a=0;a<t.length;a+=1)this._buffer8[a]=t.charCodeAt(a)}end(e=!1){const t=this._bufferLength,r=this._buffer8,a=this._buffer32,h=1+(t>>2);this._dataLength+=t;const i=8*this._dataLength;if(r[t]=128,r[t+1]=r[t+2]=r[t+3]=0,a.set(s.buffer32Identity.subarray(h),h),t>55&&(s._md5cycle(this._state,a),a.set(s.buffer32Identity)),i<=4294967295)a[14]=i;else{const e=i.toString(16).match(/(.*?)(.{0,8})$/);if(null===e)return;const t=parseInt(e[2],16),r=parseInt(e[1],16)||0;a[14]=t,a[15]=r}return s._md5cycle(this._state,a),e?this._state:s._hex(this._state)}}if(s.stateIdentity=new Int32Array([1732584193,-271733879,-1732584194,271733878]),s.buffer32Identity=new Int32Array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),s.hexChars="0123456789abcdef",s.hexOut=[],s.onePassHasher=new s,"5d41402abc4b2a76b9719d911017c592"!==s.hashStr("hello"))throw new Error("Md5 self test failed.");class a{constructor(e,t=!0,r=1048576){this._callback=e,this._async=t,this._partSize=r,this._configureReader()}hash(e){const t=this;t._blob=e,t._part=0,t._md5=new s,t._processPart()}_fail(){this._callback({success:!1,result:"data read failed"})}_hashData(e){let t=this;t._md5.appendByteArray(new Uint8Array(e.target.result)),t._part*t._partSize>=t._blob.size?t._callback({success:!0,result:t._md5.end()}):t._processPart()}_processPart(){const e=this;let t,r=0;e._part+=1,e._blob.size>e._partSize?(r=e._part*e._partSize,r>e._blob.size&&(r=e._blob.size),t=e._blob.slice((e._part-1)*e._partSize,r)):t=e._blob,e._async?e._reader.readAsArrayBuffer(t):setTimeout((()=>{try{e._hashData({target:{result:e._reader.readAsArrayBuffer(t)}})}catch(t){e._fail()}}),0)}_configureReader(){const e=this;e._async?(e._reader=new FileReader,e._reader.onload=e._hashData.bind(e),e._reader.onerror=e._fail.bind(e),e._reader.onabort=e._fail.bind(e)):e._reader=new FileReaderSync}}class h{constructor(e,t){this._queue=[],this._ready=!0;const r=this;Worker?(r._hashWorker=new Worker(e,t),r._hashWorker.onmessage=r._recievedMessage.bind(r),r._hashWorker.onerror=e=>{r._ready=!1,console.error("Hash worker failure",e)}):(r._ready=!1,console.error("Web Workers are not supported in this browser"))}hash(e){const t=this;let r;return r=new Promise(((r,s)=>{t._queue.push({blob:e,resolve:r,reject:s}),t._processNext()})),r}terminate(){this._ready=!1,this._hashWorker.terminate()}_processNext(){this._ready&&!this._processing&&this._queue.length>0&&(this._processing=this._queue.pop(),this._hashWorker.postMessage(this._processing.blob))}_recievedMessage(e){var t,r;const s=e.data;s.success?null===(t=this._processing)||void 0===t||t.resolve(s.result):null===(r=this._processing)||void 0===r||r.reject(s.result),this._processing=void 0,this._processNext()}}}}]);