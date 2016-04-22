import {Component, OnInit} from 'angular2/core';
import {ROUTER_DIRECTIVES} from 'angular2/router';

import {MATERIAL_DIRECTIVES, MATERIAL_PROVIDERS} from 'ng2-material/all';

import {EventsService} from './events.service';
import {Event} from './event';


@Component({
    selector: 'events-list',
    templateUrl: '/static/templates/events-list.html',
    directives: [ROUTER_DIRECTIVES, MATERIAL_DIRECTIVES],
    providers: [
        EventsService,
        MATERIAL_PROVIDERS
    ]
})

export class EventsListComponent implements OnInit {
    constructor(private _eventsService: EventsService) {}

    errorMessage: string;
    events: Event[];

    ngOnInit() {
        this.getEvents();
    }

    getEvents() {
        this._eventsService.getEvents()
            .then(
                events => this.events = events,
                error => this.errorMessage = <any>error);
    }
}
