import {Injectable} from 'angular2/core';
import {HTTP_PROVIDERS, Http, Response, Request, RequestMethod, Headers} from 'angular2/http';
import {Lesson} from './lesson';
import {Observable}     from 'rxjs/Observable';


@Injectable()
export class LessonService {

    constructor(private http: Http) { }

    _lessonsUrl = '/api/lessons/?limit=50';
    _lessonUrl = '/api/lessons/';

    getAllLessons() {
        return this.http.get(this._lessonsUrl)
                        .toPromise()
                        .then(res => <Lesson[]> res.json().results, this.handleError)
                        .then(lessons => {
                            console.log(lessons);
                            return lessons;
                        });
    }

    private handleError(error: Response) {
        console.error(error);
        return Observable.throw(error.json().error || 'Server error');
    }
}
