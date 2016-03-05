import {Component} from 'angular2/core';
import {RouteConfig, ROUTER_DIRECTIVES} from 'angular2/router';

import {StudentRegformComponent} from './student-regform.component';

@Component({
  selector: 'register',
  template: `
    <h1>Register</h1>
    <a [routerLink]="['RegisterStudent']">Я студент</a>
    <a href="#">Я викладач</a>
    <router-outlet></router-outlet>
  `,
  directives: [ROUTER_DIRECTIVES]
})

@RouteConfig([
  {path:'/', name: 'RegisterStudent', component: StudentRegformComponent, useAsDefault: true}
])
export class RegisterComponent { }