export enum PagePaths {
  LOGIN_PAGE = '/login',
  DASHBOARD_PAGE = '/',
  GASTROS_PAGE_CLOSED = '/gastros/closed',
  GASTROS_PAGE_SUBMISSIONS = '/gastros/submissions',
  GASTRO_PAGE_EDIT = '/gastro/:id([0-9a-z]{32})/edit',
  GASTRO_PAGE_NEW = '/gastro/new',
  PAGE_NOT_FOUND = '*',
  PROFILE_PAGE = '/profile'
}
