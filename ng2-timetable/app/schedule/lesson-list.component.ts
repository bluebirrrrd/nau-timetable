import {Component, OnInit} from 'angular2/core';

import {MATERIAL_DIRECTIVES, MATERIAL_PROVIDERS, MATERIAL_BROWSER_PROVIDERS} from 'ng2-material/all';

import {ScheduleService} from './schedule.service';
import {Schedule} from './schedule';

@Component({
    selector: 'lesson-list',
    templateUrl: '/static/templates/lesson-list.html',
    directives: [MATERIAL_DIRECTIVES],
    providers: [
        ScheduleService,
        MATERIAL_PROVIDERS,
        MATERIAL_BROWSER_PROVIDERS
    ]
})

export class LessonListComponent implements OnInit {
    constructor(private _scheduleService: ScheduleService) {}

    errorMessage: string;
    schedule: Schedule;

    ngOnInit() {
        this.getGroupSchedule('111');
    }

    getGroupSchedule(groupId: string) {
        this._scheduleService.getGroupSchedule(groupId)
            .then(
                schedule => this.schedule = schedule,
                error => this.errorMessage = <any>error);
        console.log(this.schedule);
    }

}
