import { configureStore, getDefaultMiddleware } from '@reduxjs/toolkit';
import createSagaMiddleware from 'redux-saga';
import rootReducer from 'store/reducers/rootReducer';
import rootSaga from 'store/sagas/rootSaga'

const sagaMiddleware = createSagaMiddleware();
const middleware = [...getDefaultMiddleware({ thunk: false }), sagaMiddleware];

const store = configureStore({
  reducer: rootReducer,
  devTools: true,
  middleware
});
sagaMiddleware.run(rootSaga);

export default store;
