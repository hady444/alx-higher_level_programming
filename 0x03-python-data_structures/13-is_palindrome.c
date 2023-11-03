#include "lists.h"
int checker(listint_t **head, listint_t *last);
/**
 * is_palindrome - check if palindrom list
 * @head: head of linked list
 * Return: 1 if palindrom , 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (!(*head) || !head)
		return (1);
	return (checker(head, *head));
}
/**
 * checker - Recursive function to
 * @head: pointer to head of list
 * @last: point to node at the end of list
 * Return: 1 if palindrom
 *         zero otherwise
 */
int checker(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (checker(head, last->next) && ((*head)->n == last->n))
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
