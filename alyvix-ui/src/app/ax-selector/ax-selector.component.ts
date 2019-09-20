import { Component, OnInit, ViewChild, Inject} from '@angular/core';
import { ResizedEvent } from 'angular-resize-event';
import { AxTableComponent, RowVM } from './ax-table/ax-table.component';
import { environment } from 'src/environments/environment';
import { AlyvixApiService } from '../alyvix-api.service';
import { Utils } from '../utils';
import { AxSelectorComponentGroups, AxSelectorObjects } from '../ax-model/model';
import { empty } from 'rxjs';
import { SelectorUtils } from './selector-utils';
import { GlobalRef } from './global';
import { connectableObservableDescriptor } from 'rxjs/internal/observable/ConnectableObservable';
import { SelectorDatastoreService, AxFile } from './selector-datastore.service';



@Component({
    selector: 'ax-selector',
    templateUrl: './ax-selector.component.html',
    styleUrls: ['./ax-selector.component.scss']
  })
  export class AxSelectorComponent implements OnInit {


    constructor(
      private datastore: SelectorDatastoreService
      ) {}

    selected: AxFile = {data: [], name: '', readonly: false};
    main: AxFile = {data: [], name: '', readonly: false};
    files: AxFile[] = [];
    production: boolean = environment.production;



    ngOnInit(): void {
      this.datastore.load();
      this.datastore.getWorkingCase().subscribe( workingCase => {
        if(workingCase) {
          this.main = workingCase;
          this.selected = workingCase;
        }
      });
    }


    @ViewChild(AxTableComponent) table;
    onResized(event: ResizedEvent) {
      if (this.table) {
        this.table.onResized(event);
      }
    }

    selectTab(i: AxFile) {
      this.selected = i;
    }

    closeTab(i: AxFile) {
      this.selectTab(this.main);
      this.files = this.files.filter(f => f.name !== i.name);
    }

    @ViewChild('file') _file;
    loadFile() {
      this._file.nativeElement.click();
    }

    onFileAdd() {
      const self = this;
      const files: { [key: string]: File } = this._file.nativeElement.files;
      let file:File
      for (let key in files) {
        if (!isNaN(parseInt(key))) {
          file = files[key];
          const reader = new FileReader();
          reader.onload = function() {
            if (typeof reader.result == "string") {
              self.parseFile(file.name, reader.result);
            }
          };
          reader.readAsText(file);
        }
      }
    }

    parseFile(filename: string, body: string) {
      const newFile:AxFile = {
        data: this.datastore.modelToData(JSON.parse(body)),
        readonly: true,
        name: filename.substring(0, filename.indexOf('.alyvix'))
      }
      this.files.push(newFile);
    }

    onImport(rows: RowVM[]) {
      console.log(rows);
      SelectorUtils.duplicateRows(rows, this.main.data);
    }

  }