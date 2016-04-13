import {Component} from 'angular2/core';
import {RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS} from 'angular2/router';
import {HTTP_PROVIDERS}    from 'angular2/http';
import {MATERIAL_DIRECTIVES} from 'ng2-material/all';
import {ScheduleComponent} from './schedule/schedule.component';
import {RoomSearchComponent} from './room-search/room-search.component';
import {RegisterComponent} from './register/register.component';

@Component({
  selector: 'timetable-app',
  templateUrl: 'static/templates/app.html',
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
export class AppComponent {

}
