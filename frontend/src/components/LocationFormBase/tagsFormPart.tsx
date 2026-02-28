import { Chip, FormControl, InputLabel, MenuItem, Select } from '@mui/material';
import Typography from '@mui/material/Typography';

import { Field, type FieldProps } from 'formik';

const TagsFormPart = ({ tagList }: { tagList: string[] }) => {
  return (
    <>
      <Typography variant="h5">Tags</Typography>
      <Field name="tags">
        {({ field, form, meta }: FieldProps) => (
          <FormControl variant="standard" fullWidth error={meta.touched && Boolean(meta.error)}>
            <InputLabel id="tags-select-label">Tags</InputLabel>
            <Select
              {...field}
              labelId="tags-select-label"
              id="tags-select"
              multiple
              label="Tags"
              value={field.value || []}
              onChange={(event) => {
                form.setFieldValue(field.name, event.target.value);
              }}
              renderValue={(selected: string[]) => (
                <div style={{ display: 'flex', flexWrap: 'wrap' }}>
                  {selected.map((value) => (
                    <Chip key={value} label={value} sx={{ m: 0.5 }} />
                  ))}
                </div>
              )}
            >
              {tagList.map((tag) => (
                <MenuItem key={tag} value={tag}>
                  {tag}
                </MenuItem>
              ))}
            </Select>
            {meta.touched && meta.error && (
              <Typography color="error" variant="caption">
                {meta.error}
              </Typography>
            )}
          </FormControl>
        )}
      </Field>
    </>
  );
};

export default TagsFormPart;
