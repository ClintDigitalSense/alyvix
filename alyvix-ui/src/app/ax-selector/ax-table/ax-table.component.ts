import { Component, OnInit, Inject, ViewChild, ElementRef } from '@angular/core';
import { AxSelectorObject, AxSelectorObjects, AxSelectorComponentGroups } from 'src/app/ax-model/model';
import { DomSanitizer } from '@angular/platform-browser';
import { GlobalRef } from '../global';
import { AlyvixApiService } from 'src/app/alyvix-api.service';
import { environment } from 'src/environments/environment';
import { ResizedEvent } from 'angular-resize-event';


import * as _ from 'lodash';
import { Utils } from 'src/app/utils';

interface RowVM{
  name:string
  object:AxSelectorObject
  selectedResolution:string,
  id:string
}

interface SortDescriptor{
  column: string
  asc: boolean
}


@Component({
  selector: 'ax-table',
  templateUrl: './ax-table.component.html',
  styleUrls: ['./ax-table.component.scss']
})
export class AxTableComponent implements OnInit {

  constructor(private _sanitizer: DomSanitizer,@Inject('GlobalRef') private global: GlobalRef,private apiService:AlyvixApiService) {}


  production:boolean = environment.production;
  model:AxSelectorObjects
  data: RowVM[];
  sort:SortDescriptor = {column: 'name', asc: true};
  filteredData: RowVM[];
  selectedRow:RowVM;
  resolutions: string[]

  currentResolution:string = this.global.nativeGlobal().res_string;
  selectedResolution = this.currentResolution;
  searchElementQuery = '';


  private firstResolution(component: {[key:string]:AxSelectorComponentGroups}):string {
    return Object.entries(component).map(
      ([key, value]) =>  {
         return key
      }
    )[0]
  }

  private resolutionsForObject(component: {[key:string]:AxSelectorComponentGroups}):string[] {
    return Object.entries(component).map(
      ([key, value]) =>  {
         return key
      }
    );
  }

  objectKeys = Object.keys;

  imageFor(image:string) {
    return this._sanitizer.bypassSecurityTrustResourceUrl("data:image/png;base64,"+image);
  }

  changeObjectName(oldKey: string,newKey: string) {
    delete Object.assign(this.model.objects, {[newKey]: this.model.objects[oldKey] })[oldKey];
    delete Object.assign(this.data, {[newKey]: this.data })[oldKey];
  }

  @ViewChild('tableContainer') tableContainer: ElementRef;
  onResized(event: ResizedEvent) {
    this.tableContainer.nativeElement.style.height = (event.newHeight - 44 - 70) + "px"
  }

  private prepareModelForSubmission():AxSelectorObjects {
    const model:AxSelectorObjects = { objects: {}};
    this.data.forEach( d => {
      model.objects[d.name] = d.object;
    });
    return model;
  }

  ok() {
    this.apiService.setLibrary({library: this.prepareModelForSubmission(), close_selector: true}).subscribe(x => console.log(x));
  }

  cancel() {
      this.global.nativeGlobal().cancel_button()
  }

  edit() {
    this.apiService.setLibrary({library: this.prepareModelForSubmission(), close_selector: false}).subscribe(x => {
      console.log(x);
      if(x.success) {
        this.global.nativeGlobal().edit(this.selectedRow.name,this.selectedRow.selectedResolution);
      }
    })

  }

  delay:number = 0;
  newObject() {
    this.global.nativeGlobal().new_button(this.delay);
  }

  changeTransactionGroup(row:RowVM,tg:string) {
    if(tg.length == 0) {
      row.object.measure.group = null;
    } else {
      row.object.measure.group = tg;
    }
  }

  selectRow(row) {
    this.selectedRow = row;
  }

  sortColumn(column) {
    if (this.sort.column === column) {
      this.sort.asc = !this.sort.asc;
    } else {
      this.sort = {column: column, asc: true};
    }
    this.filterData();
  }

  changeResolution() {
    this.data.forEach(d => {
      const resolutions = this.resolutionsForObject(d.object.components);
      if(resolutions.includes(this.selectedResolution)) { //select the current resolution
        d.selectedResolution = this.selectedResolution;
      } else {                                            //or the first resolution in the list
        d.selectedResolution = resolutions[0];
      }
    });
    this.filterData();
  }

  filterData() {
    let self = this;
    this.filteredData = this.data.filter( d => //resolution filter
      this.selectedResolution == 'All' ||
      this.resolutionsForObject(d.object.components).includes(this.selectedResolution)
    ).filter(d => //name filtering
      d.object.date_modified.includes(this.searchElementQuery) || d.name.includes(this.searchElementQuery)
    ).sort((r1,r2) => {

      function compare(toColumn:(RowVM) => string):number {
        if(self.sort.asc) {
          return toColumn(r1).localeCompare(toColumn(r2));
        } else {
          return -toColumn(r1).localeCompare(toColumn(r2));
        }
      }

      switch(self.sort.column) {
        case 'name': return compare(x => x.name);
        case 'transaction_group': return compare(x => x.object.measure.group);
        case 'date': return compare(x => x.object.date_modified);
      }
    })

    if((!this.filteredData.map(x => x.id).includes(this.selectedRow.id)) && this.filteredData.length > 0) {
      this.selectedRow = this.filteredData[0];
    }

  }

  isDuplicatedName(name:string):boolean {
    return this.data.filter(x => name == x.name).length > 1;
  }

  hasError():boolean {
    let result = true;
    if (this.data) {
      result = !this.data.every(d => {
        return d.name.length > 0 &&
        !this.isDuplicatedName(d.name) &&
        /^[a-zA-Z0-9_\- ]+$/.test(d.name);
      });
    }
    return result;
  }



  selectorColumns = ['name','transactionGroup','dateModified','timeout','break','measure','warning','critical','resolution','screen']

  ngOnInit(): void {
      this.apiService.getLibrary().subscribe( library => {
        this.model = library;
        this.data = Object.entries(this.model.objects).map(
          ([key, value]) =>  {
             if(!value.measure) {
               value.measure = {output: false, thresholds: {}}
             } else  {
                if(!value.measure.thresholds) value.measure.thresholds = {};
                if(typeof value.measure.output === 'undefined') value.measure.output = false;
             }
             return {name:key, object:value, selectedResolution: this.firstResolution(value.components), id: Utils.uuidv4()}
          }
        );
        this.selectedRow = this.data[0];
        this.resolutions = _.uniq(
          [this.currentResolution].concat(
            _.flatten(
              this.data.map(o => this.resolutionsForObject(o.object.components))
            )
          )
        );
        this.filterData();
      })
  }
}
