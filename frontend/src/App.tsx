import { Navigate, Route, Routes } from 'react-router-dom';

import RequireAuth from '@components/RequireAuth';

import PageContainer from './components/PageContainer';
import LoginPage from './pages/LoginPage';
import NotFoundPage from './pages/NotFoundPage';
import ProfilePage from './pages/ProfilePage';
import { PagePaths } from './pages/constants';
import GastroClosed from './pages/gastro/GastroClosedPage';
import GastroEditPage from './pages/gastro/GastroEditPage';
import GastroNewPage from './pages/gastro/GastroNewPage';
import GastroPage from './pages/gastro/GastroPage';
import GastroSubmissionsPage from './pages/gastro/GastroSubmissionPage';
import ShoppingClosedPage from './pages/shopping/ShoppingClosedPage';
import ShoppingEditPage from './pages/shopping/ShoppingEditPage';
import ShoppingNewPage from './pages/shopping/ShoppingNewPage';
import ShoppingPage from './pages/shopping/ShoppingPage';
import ShoppingSubmissionPage from './pages/shopping/ShoppingSubmissionPage';

const adminPage = (children: JSX.Element) => (
  <RequireAuth>
    <PageContainer>{children}</PageContainer>
  </RequireAuth>
);

const App = () => (
  <Routes>
    <Route path={PagePaths.LOGIN_PAGE} element={<LoginPage />} />
    <Route
      path={PagePaths.HOME}
      element={adminPage(<Navigate to={PagePaths.GASTRO_DASHBOARD} />)}
    />
    <Route path={PagePaths.GASTRO_DASHBOARD} element={adminPage(<GastroPage />)} />
    <Route path={PagePaths.GASTROS_CLOSED_PAGE} element={adminPage(<GastroClosed />)} />
    <Route
      path={PagePaths.GASTROS_SUBMISSIONS_PAGE}
      element={adminPage(<GastroSubmissionsPage />)}
    />
    <Route path={PagePaths.GASTRO_NEW_PAGE} element={adminPage(<GastroNewPage />)} />
    <Route path={PagePaths.GASTRO_EDIT_PAGE} element={adminPage(<GastroEditPage />)} />
    <Route path={PagePaths.SHOPPING_PAGE} element={adminPage(<ShoppingPage />)} />
    <Route path={PagePaths.SHOPPING_CLOSED_PAGE} element={adminPage(<ShoppingClosedPage />)} />
    <Route
      path={PagePaths.SHOPPING_SUBMISSION_PAGE}
      element={adminPage(<ShoppingSubmissionPage />)}
    />
    <Route path={PagePaths.SHOPPING_NEW_PAGE} element={adminPage(<ShoppingNewPage />)} />
    <Route path={PagePaths.SHOPPING_PAGE_EDIT} element={adminPage(<ShoppingEditPage />)} />
    <Route path={PagePaths.PROFILE_PAGE} element={adminPage(<ProfilePage />)} />
    <Route path={PagePaths.NOT_FOUND_PAGE} element={adminPage(<NotFoundPage />)} />
  </Routes>
);

export default App;
