import {Component} from 'angular2/core';
import {RouteConfig, ROUTER_DIRECTIVES} from 'angular2/router';

import {ScheduleComponent} from './schedule/schedule.component';
import {RoomSearchComponent} from './room-search/room-search.component';
import {RegisterComponent} from './register/register.component';

@Component({
  selector: 'timetable-app',
  template: `
    <h1>App Component</h1>
    <nav>
    <a [routerLink]="['Register']">Рєстрація</a>
    </nav>
    <router-outlet></router-outlet>
  `,
  directives: [ROUTER_DIRECTIVES]
})

@RouteConfig([
  {path:'/', name: 'Schedule', component: ScheduleComponent},
  {path:'/room-search', name: 'RoomSearch', component: RoomSearchComponent},
  {path:'/register/...', name: 'Register', component: RegisterComponent}
])
export class AppComponent { }