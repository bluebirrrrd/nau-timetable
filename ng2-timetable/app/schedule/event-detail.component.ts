import {Component, OnInit} from 'angular2/core';
import {RouteParams, ROUTER_DIRECTIVES} from 'angular2/router';
import {MATERIAL_DIRECTIVES, MATERIAL_PROVIDERS} from 'ng2-material/all';

import {EventsService} from './events.service';
import {Event} from './event';

@Component({
    selector: 'event-detail',
    templateUrl: 'static/templates/event-detail.html',
    styleUrls: ['https://justindujardin.github.io/ng2-material/examples/app.css',
                'static/js/lib/ng2-material/dist/ng2-material.css'],
    directives: [
        ROUTER_DIRECTIVES,
        MATERIAL_DIRECTIVES
    ],
    providers: [
        EventsService,
        MATERIAL_PROVIDERS
    ]
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
