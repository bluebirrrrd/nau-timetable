import {View, Component, OnInit} from 'angular2/core';
import {ROUTER_DIRECTIVES} from 'angular2/router';

import {MATERIAL_DIRECTIVES, MATERIAL_PROVIDERS} from 'ng2-material/all';

import {EventsService} from './events.service';
/*import {Event} from './event';*/


@Component({
    selector: 'event-form',
    templateUrl: '/static/templates/event-form.html',
    directives: [ROUTER_DIRECTIVES, MATERIAL_DIRECTIVES],
    providers: [
        EventsService,
        MATERIAL_PROVIDERS
    ]
})

export class EventFormComponent implements OnInit {
    constructor(private _eventsService: EventsService) {}

    errorMessage: string;
    options: any;

    ngOnInit() {
        this.getOptions();
    }

    getOptions() {
        this._eventsService.getOptions()
            .then(
                options => this.options = options,
                error => this.errorMessage = <any>error);
    }
}
