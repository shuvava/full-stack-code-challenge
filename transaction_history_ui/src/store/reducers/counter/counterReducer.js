import { createSlice } from '@reduxjs/toolkit';

export const counterReducer = createSlice({
  name: 'counter',
  initialState: {
    value: 0,
  },
  reducers: {
    increment: state => {
      state.value += 1;
    },
    decrement: state => {
      state.value -= 1;
    },
    incrementByAmount: (state, action) => {
      state.value += action.payload;
    },
  },
});

export const selectCount = state => state.counter.value;
export const actions = counterReducer.actions;

export default counterReducer.reducer;
