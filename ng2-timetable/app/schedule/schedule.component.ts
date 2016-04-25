import {Component} from 'angular2/core';
import {RouteConfig, ROUTER_DIRECTIVES} from 'angular2/router';
import {MATERIAL_DIRECTIVES, MATERIAL_PROVIDERS} from 'ng2-material/all';

import {LessonListComponent} from './lesson-list.component';
import {EventsListComponent} from './events-list.component';
import {EventDetailComponent} from './event-detail.component';
import {EventFormComponent} from './event-form.component';

@Component({
    template: `
    <md-content class="md-padding" layout="row" layout-wrap layout-align="end start">
       <a [routerLink]="['EventForm']">
       <button md-raised-button class="md-raised md-primary">Новий захід</button>
       </a>
     </md-content>
    <router-outlet></router-outlet>`,
    directives: [ROUTER_DIRECTIVES, MATERIAL_DIRECTIVES],
    providers: [MATERIAL_PROVIDERS]
})

@RouteConfig([
    {path:'/lessons', name: 'Lessons', component: LessonListComponent, useAsDefault: true},
    {path:'/events', name: 'Events', component: EventsListComponent},
    {path:'/events/new', name: 'EventForm', component: EventFormComponent},
    {path:'/events/:id', name: 'EventDetail', component: EventDetailComponent},
])
export class ScheduleComponent { }
