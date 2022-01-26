import React, { FC, useContext, useEffect, useState } from 'react';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';
import { Field } from 'formik';
import { Select } from 'formik-material-ui';
import MenuItem from '@material-ui/core/MenuItem';
import { CircularProgress } from '@material-ui/core';
import { isEmpty } from 'ramda';
import { authorizedFetch } from '../../../utils/fetch';
import { buildReviewListUrl } from '../../../utils/utils';
import { AuthContext } from '../../../providers/UserProvider';
import { Review } from '../../../types';
import useStyles from './styles';

const reviewItem = (reviewId: number, url: string) => (
  <MenuItem value={reviewId} key={reviewId}>
    {url}
  </MenuItem>
);

type ReviewFieldType = {
  reviews: Review[];
};

const ReviewField: FC<ReviewFieldType> = ({ reviews }) => (
  <FormControl>
    <InputLabel id="review-label">Review</InputLabel>
    <Field
      component={Select}
      name="review"
      type="number"
      inputProps={{
        id: 'review',
        labelId: 'review-label',
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
  const classes = useStyles();

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
    <div className={classes.flexContainerSpinner}>
      <div className={classes.reviewLabelSpinner}>
        <InputLabel>Review</InputLabel>
      </div>
      <div>
        <CircularProgress />
      </div>
      <div className={classes.reviewRightSpinner} />
    </div>
  ) : (
    <ReviewField reviews={reviews} />
  );
};

export default ReviewFormControl;
