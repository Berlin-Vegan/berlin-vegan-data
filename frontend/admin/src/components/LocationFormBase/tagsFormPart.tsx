import React from 'react';
import { Field } from 'formik';
import { Select } from 'formik-material-ui';
import { Chip, FormControl, InputLabel, MenuItem } from '@material-ui/core';
import Typography from '@material-ui/core/Typography';
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
      <FormControl>
        <InputLabel htmlFor="tags">Tags</InputLabel>
        <Field
          component={Select}
          name="tags"
          multiple={true}
          inputProps={{
            id: 'tags',
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
      </FormControl>
    </>
  );
};

export default TagsFormPart;
