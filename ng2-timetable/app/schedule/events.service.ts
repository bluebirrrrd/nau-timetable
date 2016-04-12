import {Injectable} from 'angular2/core';
import {HTTP_PROVIDERS, Http, Response, Request, RequestMethod} from 'angular2/http';
import {Event} from './event';
import {Observable}     from 'rxjs/Observable';


@Injectable()
export class EventsService {

    constructor(private http: Http) { }

    _eventsUrl = '/api/events/?limit=50';
    _eventUrl = '/api/events/';

    _events: Event[];
    _event: Event;
    getEvents() {
        return this.http.get(this._eventsUrl)
                        .toPromise()
                        .then(res => <Event[]> res.json().results, this.handleError)
                        .then(events => {
                            console.log(events);
                            return events;
                        });
    }

    getEvent(id: number) {
        return this.http.get(this._eventUrl + id + '/')
                   .toPromise()
                   .then(res => <Event> res.json(), this.handleError)
                   .then(event => {
                       console.log(event);
                       return event;
                    });
    }

    getOptions() {
        return this.http.request(new Request({
                     method: RequestMethod.Options,
                     url: this._eventsUrl
                   }))
                   .toPromise()
                   .then(res => res.json().actions.POST, this.handleError)
                   .then(options => {
                       console.log(options);
                       return options;
                   }); 
    }

    private handleError(error: Response) {
        console.error(error);
        return Observable.throw(error.json().error || 'Server error');
    }
}
