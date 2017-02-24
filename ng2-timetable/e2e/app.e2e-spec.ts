import { Ng2TimetablePage } from './app.po';

describe('ng2-timetable App', () => {
  let page: Ng2TimetablePage;

  beforeEach(() => {
    page = new Ng2TimetablePage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
