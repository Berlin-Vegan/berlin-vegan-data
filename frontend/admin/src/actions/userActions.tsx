export enum UserActionTypes {
  LOGIN_USER = 'LOGIN_USER',
  LOGOUT_USER = 'LOGOUT_USER',
}

export interface ILoginUserAction {
  type: UserActionTypes.LOGIN_USER;
  token: string;
}

export interface ILogoutUserAction {
  type: UserActionTypes.LOGOUT_USER;
}

export type UserActions = ILoginUserAction | ILogoutUserAction;
