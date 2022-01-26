import React, { FC, useContext, useEffect, useState } from 'react';
import { isNil, pathOr } from 'ramda';
import Typography from '@material-ui/core/Typography';
import { Theme, createStyles, makeStyles } from '@material-ui/core/styles';
import { ImageList, ImageListItem } from '@material-ui/core';
import { authorizedFetch } from '../../utils/fetch';
import { buildReviewDetailUrl } from '../../utils/utils';
import { AuthContext } from '../../providers/UserProvider';
import PaperDefault from '../PaperDefault';
import { Image, Review } from '../../types';

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    review: {
      marginTop: '32px',
    },
    reviewList: {
      display: 'flex',
      flexWrap: 'wrap',
      justifyContent: 'space-around',
      overflow: 'hidden',
      backgroundColor: theme.palette.background.paper,
    },
  }),
);

type ReviewComponentType = {
  reviewId: number;
};

export const ReviewComponent: FC<ReviewComponentType> = ({ reviewId }) => {
  const classes = useStyles();
  const { dispatch } = useContext(AuthContext);
  const [review, setReview] = useState<null | Review>(null);

  const reviewText: string = pathOr('', ['text'], review);
  const images: Image[] = pathOr([], ['images'], review);

  useEffect(() => {
    const fetchData = async () => {
      const res = await authorizedFetch(
        dispatch,
        buildReviewDetailUrl(reviewId),
      );
      const data = await res.json();
      if (res.status === 200) {
        setReview(data);
      }
    };
    fetchData();
  }, [reviewId, dispatch]);

  return (
    <div className={classes.review}>
      <PaperDefault>
        <Typography variant="h5">Review</Typography>
        <p>{reviewText}</p>
        <div className={classes.reviewList}>
          <ImageList rowHeight={310} cols={3}>
            {images.map((item: Image) => (
              <ImageListItem key={item.url} cols={1}>
                <img src={item.url} alt="" />
              </ImageListItem>
            ))}
          </ImageList>
        </div>
      </PaperDefault>
    </div>
  );
};

const getReview = (reviewId: null | number) =>
  isNil(reviewId) ? null : <ReviewComponent reviewId={reviewId} />;

export default getReview;
