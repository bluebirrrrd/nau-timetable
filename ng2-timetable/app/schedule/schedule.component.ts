import {Component} from 'angular2/core';
import {RouteConfig, ROUTER_DIRECTIVES} from 'angular2/router';
import {EventsListComponent} from './events-list.component';
import {EventDetailComponent} from './event-detail.component';
import {EventFormComponent} from './event-form.component';

@Component({
    template: `Ololo
     <a [routerLink]="['EventForm']">Новий захід</a>
    <router-outlet></router-outlet>`,
    directives: [ROUTER_DIRECTIVES]
})

@RouteConfig([
    {path:'/events', name: 'Events', component: EventsListComponent, useAsDefault: true},
    {path:'/events/new', name: 'EventForm', component: EventFormComponent},
    {path:'/events/:id', name: 'EventDetail', component: EventDetailComponent},
])
export class ScheduleComponent { }
