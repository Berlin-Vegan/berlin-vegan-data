import GastroDetailValid from './fixtures/GastroDetailVaild.json';
import gastroFormSchema from '../formSchema';

test('valid gastro object', () => {
  return gastroFormSchema
    .validate(GastroDetailValid)
    .then((result) => expect(result).toBeTruthy());
});
