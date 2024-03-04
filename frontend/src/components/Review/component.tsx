import { useContext, useEffect, useState } from 'react';

import { ImageList, ImageListItem } from '@mui/material';
import Typography from '@mui/material/Typography';

import PaperDefault from '@components/PaperDefault';
import { styles } from '@components/Review/styles';
import { isNil, pathOr } from 'ramda';

import { AuthContext } from '@/providers/UserProvider';
import { Image, Review } from '@/types';
import { authorizedFetch } from '@/utils/fetch';
import { buildReviewDetailUrl } from '@/utils/utils';

type ReviewComponentType = {
  reviewId: number;
};

export const ReviewComponent = ({ reviewId }: ReviewComponentType) => {
  const { dispatch } = useContext(AuthContext);
  const [review, setReview] = useState<null | Review>(null);

  const reviewText: string = pathOr('', ['text'], review);
  const images: Image[] = pathOr([], ['images'], review);

  useEffect(() => {
    const fetchData = async () => {
      const res = await authorizedFetch(dispatch, buildReviewDetailUrl(reviewId));
      const data = await res.json();
      if (res.status === 200) {
        setReview(data);
      }
    };
    fetchData();
  }, [reviewId, dispatch]);

  return (
    <div css={styles.review}>
      <PaperDefault>
        <Typography variant="h5">Review</Typography>
        <p>{reviewText}</p>
        <div css={styles.reviewList}>
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
