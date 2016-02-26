import {Component} from 'angular2/core';
import {RouteConfig, ROUTER_DIRECTIVES} from 'angular2/router';

import {ScheduleComponent} from './schedule/schedule.component';
import {RoomSearchComponent} from './room-search/room-search.component';

@Component({
  selector: 'timetable-app',
  template: `
    <h1>App Component</h1>
    <router-outlet></router-outlet>
  `,
  directives: [ROUTER_DIRECTIVES]
})

@RouteConfig([
  {path:'/', name: 'Schedule', component: ScheduleComponent},
  {path:'/room-search', name: 'RoomSearch', component: RoomSearchComponent}
])
export class AppComponent { }