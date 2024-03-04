import { Chip, FormControl, InputLabel, MenuItem } from '@mui/material';
import Typography from '@mui/material/Typography';

import { Field } from 'formik';
import { Select } from 'formik-mui';

import useStyles from './styles';

const tagMenuItem = (tag: string) => (
  <MenuItem key={tag} value={tag}>
    {tag}
  </MenuItem>
);

const TagsFormPart = ({ tagList }: { tagList: string[] }) => {
  const classes = useStyles();
  return (
    <>
      <Typography variant="h5">Tags</Typography>
      <Field
        component={Select}
        label="Tags"
        name="tags"
        multiple={true}
        variant="standard"
        inputProps={{
          id: 'tags-select',
          name: 'tags',
        }}
        renderValue={(selected: string[]) => (
          <div className={classes.chips}>
            {selected.map((value) => (
              <Chip key={value} label={value} className={classes.chip} />
            ))}
          </div>
        )}
      >
        {tagList.map((tag) => tagMenuItem(tag))}
      </Field>
    </>
  );
};

export default TagsFormPart;
