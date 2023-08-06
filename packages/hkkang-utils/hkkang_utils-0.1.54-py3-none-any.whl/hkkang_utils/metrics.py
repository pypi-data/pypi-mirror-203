from typing import Any, List, Tuple, Union


def compute_f1(preds: List[Any], labels: List[Any], compare_func: Any=lambda *k: k[0] == k[1], return_cnt=False) -> Union[Tuple[float, float, float], Tuple[float, float, float, float, float, float]]:
    """Compute F1 score for between two lists of items. Order of the items in the lists does not matter."""
    tp, fp, fn = 0, 0, 0
    # Count tp, fp, fn
    label_indices = [i for i in range(len(labels))]
    for pred in preds:
        found = False
        # Check if pred is in labels
        for i in label_indices:
            if compare_func(pred, labels[i]):
                tp += 1
                label_indices.remove(i)
                found= True
                break
        if not found:
            fp += 1
    fn = len(label_indices)
    # Compute f1, precision, recall
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * precision * recall / (precision + recall)
    if return_cnt:
        return f1, precision, recall, tp, fp, fn
    else:
        return f1, precision, recall