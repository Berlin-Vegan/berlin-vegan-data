import { Reducer } from 'redux';
import { UserActionTypes, UserActions } from '../actions/userActions';

export interface IUserState {
  readonly authenticated: boolean;
}

const initialUserState: IUserState = {
  authenticated: false,
};

export const userReducer: Reducer<IUserState, UserActions> = (
  state = initialUserState,
  action
) => {
  switch (action.type) {
    case UserActionTypes.LOGIN_USER: {
      return {
        ...state,
        authenticated: true,
      };
    }
    case UserActionTypes.LOGOUT_USER: {
      return {
        authenticated: false,
      };
    }
    default:
      return state;
  }
};
