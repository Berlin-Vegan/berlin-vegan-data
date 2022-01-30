import renderer from 'react-test-renderer';
import React, { ComponentType } from 'react';
import ReactDOM from 'react-dom';
import { act } from 'react-dom/test-utils';

export const standardComponentTest = (C: ComponentType<any>, props = {}) => {
  renderWithTestRenderer(C, props);
  it('renders without crashing', () => renders(C, props));
};

export const standardComponentTestMockFetch = (
  C: ComponentType<any>,
  props = {},
  fakeResponse: any,
) => {
  renderWithTestRenderer(C, props);
  it('renders without crashing and mock fetch', async () => {
    jest.spyOn(window, 'fetch').mockImplementation((): Promise<any> => {
      const fetchResponse = {
        json: () => Promise.resolve(fakeResponse),
      };
      return Promise.resolve(fetchResponse);
    });
    await act(async () => renders(C, props));
  });
};

export const renders = (C: ComponentType, props: object) => {
  const div = document.createElement('div');
  ReactDOM.render(<C {...props} />, div);
};

const getName = (C: ComponentType) => C.displayName || C.name || 'A Component';

const renderWithTestRenderer = (C: ComponentType, props: object) => {
  it(`render <${getName(C)} />`, () => {
    const tree = renderer.create(<C {...props} />).toJSON();
    expect(tree).toMatchSnapshot();
  });
};
