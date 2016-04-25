import {Component, OnInit} from 'angular2/core';

import {MATERIAL_DIRECTIVES, MATERIAL_PROVIDERS, MATERIAL_BROWSER_PROVIDERS} from 'ng2-material/all';

import {LessonService} from './lesson.service';
import {Lesson} from './lesson';

@Component({
    selector: 'lesson-list',
    templateUrl: '/static/templates/lesson-list.html',
    directives: [MATERIAL_DIRECTIVES],
    providers: [
        LessonService,
        MATERIAL_PROVIDERS,
        MATERIAL_BROWSER_PROVIDERS
    ]
})

export class LessonListComponent implements OnInit {
    constructor(private _lessonService: LessonService) {}

    errorMessage: string;
    lessons: Lesson[];

    ngOnInit() {
        this.getLessons();
    }

    getLessons() {
        this._lessonService.getAllLessons()
            .then(
                lessons => this.lessons = lessons,
                error => this.errorMessage = <any>error);
    }
}