import {Component, OnInit, ElementRef} from 'angular2/core';
import {ROUTER_DIRECTIVES, Router} from 'angular2/router';

import {MATERIAL_DIRECTIVES, MATERIAL_PROVIDERS, MdDialog} from 'ng2-material/all';
import {MdDialogConfig, MdDialogBasic, MdDialogRef} from 'ng2-material/components/dialog/dialog';

import {EventsService} from './events.service';
import {Event} from './event';



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
    constructor(private _eventsService: EventsService,
                private _router: Router,
                public dialog: MdDialog,
                public element: ElementRef) {}

    errorMessage: string;
    options: any;
    event: Event = new Event();

    ngOnInit() {
        this.getOptions();
    }

    getOptions() {
        this._eventsService.getOptions()
            .then(
                options => this.options = options,
                error => this.errorMessage = <any>error);
    }

    onSubmit() {
        this.addEvent(this.event);
        this._router.navigate(['Events']);

    }

    addEvent(event: Event) {
        let res = this._eventsService.addEvent(event)
            .then(
                result => res = result,
                error => this.errorMessage = <any>error);
    }

    showConfirm() {
    let config = new MdDialogConfig()
      .textContent('Ви впевнені, що хочете очистити форму?')
      .clickOutsideToClose(false)
      .title('Стерти дані?')
      .ariaLabel('Підтвердження')
      .ok('Стерти!')
      .cancel('Ні, повернутись до даних');
    this.dialog.open(MdDialogBasic, this.element, config)
      .then((ref: MdDialogRef) => {
        ref.whenClosed.then((result) => {
          if (result) {
            this.event = new Event();
          }
        })
      });
    }
}
