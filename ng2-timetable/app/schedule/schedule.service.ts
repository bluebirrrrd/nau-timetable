import {Injectable} from 'angular2/core';
import {HTTP_PROVIDERS, Http, Response, Request, RequestMethod, Headers} from 'angular2/http';
import {Observable} from 'rxjs/Observable';
import {Schedule} from './schedule';
import {Week} from './week.schedule';


@Injectable()
export class ScheduleService {

    constructor(private http: Http) { }

    _lessonsUrl = '/api/schedule/?limit=50';
    _groupScheduleUrl = '/api/group/schedule/';

    getGroupSchedule(groupId: string) {
        return this.http.get(this._groupScheduleUrl + groupId)
                        .toPromise()
                        .then(res => res.json(), this.handleError)
                        .then(json => <Schedule> {
                          first: <Week> json['true'],
                          second: <Week> json['false']
                        });
    }

    private handleError(error: Response) {
        console.error(error);
        return Observable.throw(error.json().error || 'Server error');
    }
}
