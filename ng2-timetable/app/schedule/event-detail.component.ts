import {Component, OnInit} from 'angular2/core';
import {RouteParams} from 'angular2/router';

import {EventsService} from './events.service';
import {Event} from './event';

@Component({
    selector: 'event-detail',
    templateUrl: 'static/templates/event-detail.html',
    providers: [EventsService]
})

export class EventDetailComponent implements OnInit {
    constructor(
        private _eventsService: EventsService,
        private _routeParams: RouteParams) {}

    errorMessage: string;
    event: Event;

    ngOnInit() {
        let id = +this._routeParams.get('id');
        this.getEvent(id);
    }

    getEvent(id: number) {
        return this._eventsService.getEvent(id)
            .then(
                event => {
                    console.log(event);
                    this.event = event;
                },
                error => this.errorMessage = <string>error);
    }
 }
