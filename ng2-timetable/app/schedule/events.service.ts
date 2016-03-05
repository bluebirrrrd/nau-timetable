import {Injectable} from 'angular2/core';
import {Http, Response} from 'angular2/http';
import {Event} from './event';
import {Observable}     from 'rxjs/Observable';

@Injectable()
export class EventsService {

    constructor(private http: Http) { }

    _eventsUrl = '/api/events/?limit=50';

    getEvents() {
        return this.http.get(this._eventsUrl)
                        .toPromise()
                        .then(res => <Event[]> res.json().results, this.handleError)
                        .then(events => {
                            console.log(events);
                            return events;
                        });
    }

    private handleError(error: Response) {
        console.error(error);
        return Observable.throw(error.json().error || 'Server error');
        
    }
}