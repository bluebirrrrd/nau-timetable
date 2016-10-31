import {Component} from 'angular2/core';
import {RouteConfig, ROUTER_DIRECTIVES} from 'angular2/router';

import {StudentRegformComponent} from './student-regform.component';
import {RegistrationComponent} from './registration.component';

@Component({
  selector: 'register',
  template: `
    <h1 style="text-align: center">Реєстрація</h1>
    <regForm></regForm>
    <router-outlet></router-outlet>
  `,
  directives: [ROUTER_DIRECTIVES]
})

@RouteConfig([
  {path:'/', name: 'Reg', component: RegistrationComponent, useAsDefault: true}
])
export class RegisterComponent { }
