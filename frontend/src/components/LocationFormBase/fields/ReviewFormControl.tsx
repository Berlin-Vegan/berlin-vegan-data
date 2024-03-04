import { useContext, useEffect, useState } from 'react';

import { CircularProgress, FormControl } from '@mui/material';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';

import { Field } from 'formik';
import { Select } from 'formik-mui';
import { isEmpty } from 'ramda';

import { AuthContext } from '@/providers/UserProvider';
import { Review } from '@/types';
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

const ReviewField = ({ reviews }: ReviewFieldType) => (
  <FormControl fullWidth={true}>
    <Field
      component={Select}
      name="review"
      label="Review"
      variant="standard"
      inputProps={{
        id: 'review-select',
        name: 'review',
      }}
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
    <div css={styles.flexContainerSpinner}>
      <div css={styles.reviewLabelSpinner}>
        <InputLabel>Review</InputLabel>
      </div>
      <div>
        <CircularProgress />
      </div>
      <div css={styles.reviewRightSpinner} />
    </div>
  ) : (
    <ReviewField reviews={reviews} />
  );
};

export default ReviewFormControl;
