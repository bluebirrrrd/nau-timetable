import {bootstrap}    from 'angular2/platform/browser';
import {MATERIAL_DIRECTIVES, MATERIAL_PROVIDERS, MATERIAL_BROWSER_PROVIDERS} from 'ng2-material/all';
import {AppComponent} from './app.component';
import 'rxjs/Rx';



bootstrap(AppComponent, [MATERIAL_BROWSER_PROVIDERS]);
