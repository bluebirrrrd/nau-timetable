import {View, Component, OnInit, provide} from 'angular2/core';
import {EventsService} from './events.service';
import {Event} from './event';


@Component({
    selector: 'events-list',
    templateUrl: '/static/templates/events-list.html',
    providers: [
        EventsService
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
