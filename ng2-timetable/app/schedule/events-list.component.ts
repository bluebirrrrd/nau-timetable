import {View, Component, OnInit, provide} from 'angular2/core';
import {ROUTER_DIRECTIVES} from 'angular2/router';

import {MATERIAL_DIRECTIVES} from 'ng2-material/all';

import {EventsService} from './events.service';
import {Event} from './event';


@Component({
    selector: 'events-list',
    templateUrl: '/static/templates/events-list.html',
    directives: [ROUTER_DIRECTIVES],
    providers: [
        EventsService,
        MATERIAL_DIRECTIVES
    ]
})

export class EventsListComponent implements OnInit {
    constructor(private _eventsService: EventsService) {}

    errorMessage: string;
    events: Event[];

    ngOnInit() {
        // TODO: connect to the service
        this.getEvents();
    }

    getEvents() {
    this._eventsService.getEvents()
        .then(
            events => this.events = events,
            error => this.errorMessage = <any>error);
    }
}
