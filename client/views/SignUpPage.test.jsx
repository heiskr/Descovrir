import SignUpPage from './SignUpPage'

describe('SignUpPage', () => {
  it('should render the sign up page', () => {
    expect(SignUpPage({ gqlErrors: {}, body: {}, query: {} })).toMatchSnapshot()
  })
})