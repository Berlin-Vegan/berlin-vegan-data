import { combineReducers, createStore, Store, compose } from 'redux';
import { persistStore, persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage';

import { PersistConfig } from 'redux-persist/es/types';
import { IUserState, userReducer } from '../reducers/userReducer';

const userPersistConfig: PersistConfig<any> = {
  key: 'user',
  storage,
};

export interface IAppState {
  userState: IUserState;
}

const rootReducer = combineReducers<IAppState>({
  userState: persistReducer(userPersistConfig, userReducer),
});

declare global {
  interface Window {
    __REDUX_DEVTOOLS_EXTENSION_COMPOSE__?: typeof compose;
  }
}

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const configureStore = (): Store<IAppState, any> => {
  return createStore(rootReducer, undefined, composeEnhancers());
};

export const store = configureStore();
export const persistor = persistStore(store);
