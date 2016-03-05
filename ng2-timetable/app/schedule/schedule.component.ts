import {Component} from 'angular2/core';
import {RouteConfig, ROUTER_DIRECTIVES} from 'angular2/router';
import {EventsListComponent} from './events-list.component';
@Component({
    template: `Ololo
    <router-outlet></router-outlet>`,
    directives: [ROUTER_DIRECTIVES]
})

@RouteConfig([
    {path:'/events', name: 'Events', component: EventsListComponent, useAsDefault: true}
])
export class ScheduleComponent { }
