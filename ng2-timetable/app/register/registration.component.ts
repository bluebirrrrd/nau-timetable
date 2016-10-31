import {Component, OnInit, ElementRef} from 'angular2/core';
import {ROUTER_DIRECTIVES, Router} from 'angular2/router';

import {MATERIAL_DIRECTIVES, MATERIAL_PROVIDERS, MdDialog} from 'ng2-material/all';
import {MdDialogConfig, MdDialogBasic, MdDialogRef} from 'ng2-material/components/dialog/dialog';


@Component({
    selector: 'reg-form',
    templateUrl: '/static/templates/reg-form.html',
    directives: [ROUTER_DIRECTIVES, MATERIAL_DIRECTIVES],
    providers: [
        MATERIAL_PROVIDERS
    ]
})

export class RegistrationComponent {

}
