import { enableProdMode, PlatformRef, NgModuleRef } from '@angular/core';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { DesignerModule } from './app/ax-designer/designer.module';
import { environment } from './environments/environment';
import { HotkeysService } from 'angular2-hotkeys';
import { SelectorModule } from './app/ax-selector/selector.module';
import { SelectorDatastoreService } from './app/ax-selector/selector-datastore.service';
import { DesignerDatastoreService } from './app/ax-designer/designer-datastore.service';


if (environment.production) {
  enableProdMode();
}


var designer: void | NgModuleRef<DesignerModule>
var selector: void | NgModuleRef<SelectorModule>

function loadAlyvixDesigner() {
  platformBrowserDynamic().bootstrapModule(DesignerModule).catch(err => console.log(err)).then(module => designer = module)
}

function loadAlyvixSelector() {
  platformBrowserDynamic().bootstrapModule(SelectorModule).catch(err => console.log(err)).then(module => selector = module)
}

function reloadAlyvixSelector(objectName: string) {
  if (selector) {
    const selectorDatastore = selector.injector.get(SelectorDatastoreService);
    selectorDatastore.reload(objectName);
  }
}

function unloadAlyvixDesigner() {
  if (designer) {
    const hotkeyService = designer.injector.get(HotkeysService);
    hotkeyService.reset();
    designer.destroy();
  }
}

function unloadAlyvixSelector() {
  if (selector) {
    selector.destroy();
  }
}

function setExePath(path) {
  console.log("test");
  if(designer) {
    const datastore = designer.injector.get(DesignerDatastoreService);
    datastore.setSelectedFile(path);
  }
}


(window as any).loadAlyvixDesigner = loadAlyvixDesigner;
(window as any).unloadAlyvixDesigner = unloadAlyvixDesigner;
(window as any).loadAlyvixSelector = loadAlyvixSelector;
(window as any).reloadAlyvixSelector = reloadAlyvixSelector;
(window as any).unloadAlyvixSelector = unloadAlyvixSelector;
(window as any).setExePath = setExePath;

/* TO TEST
var node = document.createElement("app-root");
document.body.append(node);
loadAlyvixDesigner()
*/

if (!environment.production) {
  if(environment.workingOn == "designer") {
    loadAlyvixDesigner();
  } else if(environment.workingOn == "selector") {
    loadAlyvixSelector();
  }

  //loadAlyvixSelector();
  // uncomment o simulate multiple close open of the designer
  // setTimeout(() => {
  //   unloadAlyvixDesigner();
  //   console.log("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  //   var node = document.createElement("app-root");
  //   document.body.append(node);
  //   loadAlyvixDesigner();
  //   setTimeout(() => {
  //     unloadAlyvixDesigner();
  //     console.log("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  //     var node = document.createElement("app-root");
  //     document.body.append(node);
  //     loadAlyvixDesigner();
  //   }, 5000);
  // }, 5000);

}


