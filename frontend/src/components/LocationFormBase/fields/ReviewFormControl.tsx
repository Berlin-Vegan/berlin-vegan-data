import { useContext, useEffect, useState } from 'react';

import { CircularProgress, FormControl } from '@mui/material';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';

import BVSelect from '@components/LocationFormBase/fields/BVSelect';
import { Field } from 'formik';
import { isEmpty } from 'ramda';

import { AuthContext } from '@/providers/UserProvider';
import type { Review } from '@/types';
import { authorizedFetch } from '@/utils/fetch';
import { buildReviewListUrl } from '@/utils/utils';

import { styles } from './styles';

const reviewItem = (reviewId: number, url: string) => (
  <MenuItem value={reviewId} key={reviewId}>
    {url}
  </MenuItem>
);

type ReviewFieldType = {
  reviews: Review[];
};

const stringToReviewValue = (value: string | unknown) => {
  if (value === '') return null;

  if (typeof value == 'string') {
    return parseInt(value);
  }
  return null;
};

const reviewValueToString = (value: number | null | unknown) => {
  if (typeof value !== 'number') {
    return '';
  }
  return value.toString();
};

const ReviewField = ({ reviews }: ReviewFieldType) => (
  <FormControl fullWidth={true}>
    <Field
      component={BVSelect}
      name="review"
      label="Review"
      variant="standard"
      inputProps={{
        id: 'review-select',
        name: 'review',
      }}
      readValue={reviewValueToString}
      setValue={stringToReviewValue}
    >
      <MenuItem value="" key="">
        -------
      </MenuItem>
      {reviews.map((review) => reviewItem(review.id, review.url))}
    </Field>
  </FormControl>
);

const ReviewFormControl = () => {
  const { dispatch } = useContext(AuthContext);
  const [reviews, setReviews] = useState<Review[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const res = await authorizedFetch(dispatch, buildReviewListUrl);
      const data = await res.json();
      if (res.status === 200) {
        setReviews(data);
      }
    };
    fetchData();
  }, [dispatch]);

  return isEmpty(reviews) ? (
    <Box sx={styles.flexContainerSpinner}>
      <Box sx={styles.reviewLabelSpinner}>
        <InputLabel>Review</InputLabel>
      </Box>
      <Box>
        <CircularProgress />
      </Box>
      <Box sx={styles.reviewRightSpinner} />
    </Box>
  ) : (
    <ReviewField reviews={reviews} />
  );
};

export default ReviewFormControl;
