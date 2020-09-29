import React, { Context, createContext, useReducer, useEffect } from 'react';

const TYPE_USER_LOGIN = 'USER_LOGIN';
const TYPE_USER_LOGOUT = 'USER_LOGOUT';
const TYPE_SET_USER_DATA = 'SET_USER_DATA';
const TYPE_UPDATE_USER_EMAIL = 'UPDATE_USER_DATA';
const LOCALSTORAGE_KEY = 'UserProvider';

type UserData = { id: number; username: string; email: string } | {};
type UserAction =
  | { type: typeof TYPE_USER_LOGIN }
  | { type: typeof TYPE_USER_LOGOUT }
  | { type: typeof TYPE_SET_USER_DATA; payload: UserData }
  | { type: typeof TYPE_UPDATE_USER_EMAIL; payload: string };
type UserState = { authenticated: boolean; userData: UserData };
export type UserDispatch = (action: UserAction) => void;

interface IUserContext {
  state: UserState;
  dispatch: UserDispatch;
}

const authReducer = (state: UserState, action: UserAction) => {
  switch (action.type) {
    case TYPE_USER_LOGIN: {
      return { ...state, authenticated: true };
    }
    case TYPE_USER_LOGOUT: {
      return { userData: {}, authenticated: false };
    }
    case TYPE_SET_USER_DATA: {
      return { ...state, userData: { ...action.payload } };
    }
    case TYPE_UPDATE_USER_EMAIL: {
      return {
        ...state,
        userData: { ...state.userData, email: action.payload },
      };
    }
  }
  return state;
};

const AuthContext: Context<IUserContext> = createContext({} as IUserContext);

const initialStateDefault = { authenticated: false, userData: {} };
const initialState =
  JSON.parse(localStorage.getItem(LOCALSTORAGE_KEY) as string) ||
  initialStateDefault;

const UserProvider: React.FC = ({ children }) => {
  const [state, dispatch] = useReducer(authReducer, initialState);

  useEffect(() => {
    localStorage.setItem(LOCALSTORAGE_KEY, JSON.stringify(state));
  }, [state]);

  return (
    <AuthContext.Provider
      value={{
        state,
        dispatch,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export {
  UserProvider,
  AuthContext,
  TYPE_USER_LOGIN,
  TYPE_USER_LOGOUT,
  TYPE_SET_USER_DATA,
  TYPE_UPDATE_USER_EMAIL,
};
