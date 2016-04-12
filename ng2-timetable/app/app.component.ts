import {Component} from 'angular2/core';
import {RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS} from 'angular2/router';
import {HTTP_PROVIDERS}    from 'angular2/http';
import {MATERIAL_DIRECTIVES} from 'ng2-material/all';
import {ScheduleComponent} from './schedule/schedule.component';
import {RoomSearchComponent} from './room-search/room-search.component';
import {RegisterComponent} from './register/register.component';

@Component({
  selector: 'timetable-app',
  template: `
    <h1>App Component</h1>
    <nav>
      <a [routerLink]="['Register']">Рєстрація</a>
      <a [routerLink]="['RoomSearch']">Пошук вільної аудиторії</a>
      <a [routerLink]="['Schedule']">Розклад</a>
      <a [routerLink]="['EventForm']">Новий захід</a>
    </nav>
    <router-outlet></router-outlet>
  `,
  directives: [
    ROUTER_DIRECTIVES,
    MATERIAL_DIRECTIVES
  ],
  providers: [
    ROUTER_PROVIDERS,
    HTTP_PROVIDERS
  ]
})

@RouteConfig([
  {path:'/...', name: 'Schedule', component: ScheduleComponent, useAsDefault: true},
  {path:'/room-search', name: 'RoomSearch', component: RoomSearchComponent},
  {path:'/register/...', name: 'Register', component: RegisterComponent}
])
export class AppComponent { }
